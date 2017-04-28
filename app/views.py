from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all().values('id')
    post_id = []
    for item in articles:
        post_id.append(item['id'])

    return render(request, 'index.html', {'post': post_id})


def article(request):
    pass
