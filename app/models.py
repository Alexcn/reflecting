from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class User(BaseModel):
#     login_name = models.CharField(max_length=32, unique=True, db_index=True)
#     nick_name = models.CharField(max_length=32, blank=True, null=True)
#     cell_phone = models.CharField(max_length=24, unique=True, blank=True)
#     description = models.TextField(max_length=1024, null=True, blank=True)
#
#     class Meta:
#         db_table = 'users'


class Article(BaseModel):
    title = models.CharField(max_length=255, default='', verbose_name='文章标题')
    short_name = models.CharField(max_length=255, default='', verbose_name='地址显示')
    # author = models.CharField(max_length=32, default='', verbose_name='文章作者')
    content = UEditorField(verbose_name='文章内容', width=850, height=400, imagePath="article/ueditor/",
                           filePath="article/ueditor/", default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'articles'
        verbose_name = '文章撰写'
        verbose_name_plural = verbose_name
