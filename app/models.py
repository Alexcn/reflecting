from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.fields import StatusField
from model_utils import Choices


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    # id = models.AutoField(primary_key=True)
    login_name = models.CharField(max_length=32, unique=True, db_index=True)
    nick_name = models.CharField(max_length=32, blank=True, null=True)
    cell_phone = models.CharField(max_length=24, unique=True, blank=True)
    # email = models.CharField(max_length=254, unique=True)
    STATUS = Choices('男', '女', '保密')
    gender = StatusField(null=True)     # 需要添加状态选择变量
    role_id = models.IntegerField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # last_login = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = 'users'


class Article(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'users'
        verbose_name = '文章撰写'
        verbose_name_plural = verbose_name


class Visitor(BaseModel):
    ip = models.CharField(max_length=40)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Detail Visitor'
        verbose_name_plural = 'Visitors'
        ordering = ['-created']

