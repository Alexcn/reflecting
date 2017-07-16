from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^comment/$', CommentsView.as_view(), name='comment'),
    url(r'^reply/$', ReplyView.as_view(), name='reply'),
]
