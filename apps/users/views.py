from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from users.models import Message, EmailVerifyCode
from utils.email_send import send_password_email
from django.views.generic import View
from django.utils import timezone
from .models import UserProfile
from django.db.models import Q
from .forms import *
from utils.mixin_utils import LoginRequiredMixin

__all__ = [
    'RegisterView',
    'LoginView',
    'LogoutView',
    'PasswordView'
]


class CustomBackend(ModelBackend):
    """自定义auth验证，可以通过用户名邮箱登录"""

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # 通过用户名或邮箱获取用户是否存在
            if user.check_password(password):  # 如果用户密码正确返回user对象
                return user
            else:  # 出错或者用户密码错误就返回None
                return None
        except Exception:
            return None


# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        register_form = RegisterForm(request.POST)  # 验证传过来的参数
        if register_form.is_valid():
            email = request.POST.get('email', '')  # 获取邮箱
            try:
                UserProfile.objects.get(email=email)  # 如果邮箱已经存在
                return render(request, 'register.html', {'errors': '邮箱：%s 已存在！' % email})
            except ObjectDoesNotExist:
                password = request.POST.get('password', '')  # 获取密码
                retype_password = request.POST.get('retype_password', '')  # 确认密码
                if password == retype_password:
                    UserProfile.objects.create(username=email, email=email, password=make_password(password))
                    Message.objects.create(body="用户%s于%s进行了注册" % (email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))  # 跳转到登录页面
                else:
                    errors = '两次密码不一致~'
                    return render(request, 'register.html', {'errors': errors})
        else:
            return render(request, 'register.html', {'errors': register_form.errors})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        """验证用户是否是否可以成功登录"""
        login_form = LoginForm(request.POST)  # FORM验证传过来的值是否合法
        if login_form.is_valid():  # 验证是否错误
            email = request.POST.get('email', '')  # 获取用户名
            password = request.POST.get('password', '')  # 获取密码
            user = authenticate(username=email, password=password)  # 验证用户名和密码
            if user is not None:  # 如果用户名和密码匹配
                if user.is_active:  # 如果用户是激活状态
                    login(request, user)  # 把SESSION和COOKIE写入request
                    if user.is_superuser:
                        return HttpResponseRedirect(reverse('admin:dashboard'))  # 返回首页
                    else:
                        return HttpResponseRedirect(reverse('index'))  # 返回首页
                else:  # 用户未激活
                    return render(request, 'login.html', {'errors': '用户尚未激活！'})
            else:  # 用户名和密码错误
                return render(request, 'login.html', {'errors': '用户名或密码错误！'})
        else:  # FORM验证出错，并吧出错信息传递到前端
            return render(request, 'login.html', {'errors': login_form.errors})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class PasswordView(View):
    def get(self, request):
        code = request.GET.get('code', '')
        if code:
            try:
                EmailVerifyCode.objects.get(code=code)
                return render(request, 'password.html', {'code': code, 'flag': True})
            except EmailVerifyCode.DoesNotExist:
                return HttpResponse('重置密码链接已失效~')
        else:
            return render(request, 'password.html')

    def post(self, request):
        email = request.POST.get('email', '')
        try:
            UserProfile.objects.get(email=email)
            result = send_password_email(email=email)
            if result:
                return HttpResponse('重置密码的链接已发送至你的邮箱，请注意查收~')
            return HttpResponse('用户不存在~')
        except UserProfile.DoesNotExist:
            return HttpResponse('用户不存在~')


class RestPasswordView(View):
    def post(self, request):
        code = request.POST.get('code')  # Code
        if code:
            rest_form = RestPasswordForm(request.POST)
            if rest_form.is_valid():
                password = request.POST.get('password', '')  # 获取密码
                retype_password = request.POST.get('retype_password', '')  # 确认密码
                if password == retype_password:
                    emailverify = EmailVerifyCode.objects.get(code=code)
                    email = emailverify.email
                    user = UserProfile.objects.get(email=email)
                    user.password = make_password(password)
                    user.save()
                    emailverify.delete()
                    Message.objects.create(body="用户%s于%s修改了密码" % (email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse('两次密码不一致~')
            else:
                return HttpResponse(rest_form.errors)
        else:
            admin_password_form = AdminRestPasswordForm(request.POST)
            if admin_password_form.is_valid():
                oldpassword = request.POST.get('oldpassword')
                newpassword = request.POST.get('newpassword')
                retypepassword = request.POST.get('retypepassword')
                user = authenticate(username=request.user.email, password=oldpassword)
                if newpassword == retypepassword and user:
                    user.password = make_password(newpassword)
                    user.save()
                    logout(request)
                    Message.objects.create(body="用户%s于%s通过后台修改了密码" % (request.user.email, timezone.now()))
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse('请确保两次密码相同且旧密码正确~')
            else:
                return HttpResponse(admin_password_form.errors)
