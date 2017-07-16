from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.default_model import random_nick_name
from blog.models import Article

__all__ = [
    'UserProfile',
    'EmailVerifyCode',
    'Message',
    'Comment',
    'Reply'
]


# Create your models here.

class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知')
    )
    nick_name = models.CharField(max_length=100, default=random_nick_name)
    gender = models.CharField(choices=gender_choices, default='unknown', max_length=20)
    image = models.ImageField(upload_to='avatar/%Y/%m', max_length=100, default='avatar/avatar.png')

    def get_message_count(self):
        return Message.objects.filter(status=False).count()

    def get_comment_count(self):
        return Comment.objects.filter(status=False).count()


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    send_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200)
    status = models.BooleanField(default=False)


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article, related_name='article_comment')
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_reply(self):
        return Reply.objects.filter(comment=self.pk)


class Reply(models.Model):
    user = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(Comment)
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
