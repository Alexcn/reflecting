from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.db.models import Q
from .models import *
from .forms import *
from users.models import Comment, Reply
from utils.mixin_utils import LoginRequiredMixin

__all__ = [
    'ArticleListView',
    'ArticleDetailView',
    'CommentsView',
    'ReplyView',
    'AboutView'
]


# Create your views here.

class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(status=0).order_by('-created_time')
        search = request.GET.get('search')
        search_sm = request.GET.get('search_sm')
        if search:
            articles = articles.filter(Q(title__icontains=search) | Q(body__icontains=search))
        if search_sm:
            articles = articles.filter(Q(title__icontains=search_sm) | Q(body__icontains=search_sm))
        tag = request.GET.get('tag')
        categories = request.GET.get('category')
        if tag:
            T = Tag.objects.get(name=tag)
            articles = articles.filter(tag=T)
        if categories:
            C = Categories.objects.get(name=categories)
            articles = articles.filter(categories=C)
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 10, request=request)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        comments = Comment.objects.all().order_by('-add_time')[:5]
        links = Link.objects.all()
        categories = Categories.objects.all()
        tags = Tag.objects.all()
        reads = Article.objects.all().order_by('-read')[:5]
        try:
            setting = Setting.objects.get(pk=1)
        except Setting.DoesNotExist:
            setting = None
        return render(request, 'index.html', {'articles': articles, 'comments': comments, 'links': links, 'categories': categories, 'tags': tags, 'reads': reads, 'setting': setting})


class ArticleDetailView(View):
    def get(self, request, article_url):
        try:
            article = Article.objects.get(url=article_url)
            article.read += 1
            article.save()
            comments = Comment.objects.filter(article=article).order_by('-add_time')
            url = 'https://' + request.get_host() + request.get_full_path()
            reads = Article.objects.all().order_by('-read')[:5]
            try:
                setting = Setting.objects.get(pk=1)
            except Setting.DoesNotExist:
                setting = None
            return render(request, 'article.html', {'article': article, 'comments': comments, 'url': url, 'reads': reads, 'setting': setting})
        except Article.DoesNotExist:
            return HttpResponse('404', status=404)


class CommentsView(LoginRequiredMixin, View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            url = request.POST.get('url')
            body = request.POST.get('body')
            article = Article.objects.get(url=url)
            Comment.objects.create(article=article, user=request.user, body=body)
            return HttpResponse(status=200)
        else:
            return HttpResponse(comment_form.errors)


class ReplyView(LoginRequiredMixin, View):
    def post(self, request):
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            commentid = request.POST.get('commentid')
            body = request.POST.get('body')
            comment = Comment.objects.get(pk=commentid)
            Reply.objects.create(user=request.user, comment=comment, body=body)
            return HttpResponse()
        else:
            return HttpResponse(reply_form.errors)


class AboutView(View):
    def get(self, request):
        article = Article.objects.all().last()
        article.read += 1
        article.save()
        comments = Comment.objects.filter(article=article).order_by('-add_time')
        url = 'https://' + request.get_host() + request.get_full_path()
        reads = Article.objects.all().order_by('-read')[:5]
        try:
            setting = Setting.objects.get(pk=1)
        except Setting.DoesNotExist:
            setting = None
        return render(request, 'article.html', {
            'article': article,
            'comments': comments,
            'url': url, 'reads': reads,
            'setting': setting})
