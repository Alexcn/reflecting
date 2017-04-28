from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all().values('id')
    return render(request, 'index.html', articles)


def article(request):
    pass
