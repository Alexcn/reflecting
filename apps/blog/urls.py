from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/$', CommentsView.as_view(), name='comment'),
    url(r'^reply/$', ReplyView.as_view(), name='reply'),
]


hander404 = 'blog.views.page_not_found'
hander500 = 'blog.views.page_errors'
