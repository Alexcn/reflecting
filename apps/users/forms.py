from django import forms

__all__ = [
    'RegisterForm',
    'LoginForm',
    'RestPasswordForm',
    'AdminRestPasswordForm'
]


class RegisterForm(forms.Form):
    """注册Form验证"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    retype_password = forms.CharField(required=True, min_length=5)
    """验证两个密码是否一致"""


class LoginForm(forms.Form):
    """登录Form验证"""
    email = forms.CharField(required=True, max_length=150)  # 字符串类型，必填字段，最大长度150
    password = forms.CharField(required=True, max_length=128)  # 字符串类型，必填字段，最大长度128


class RestPasswordForm(forms.Form):
    code = forms.CharField()
    password = forms.CharField(required=True, min_length=5)
    retype_password = forms.CharField(required=True, min_length=5)


class AdminRestPasswordForm(forms.Form):
    oldpassword = forms.CharField(required=True, )
    newpassword = forms.CharField(required=True, min_length=5)
    retypepassword = forms.CharField(required=True, min_length=5)
