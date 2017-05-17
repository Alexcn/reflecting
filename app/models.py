from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    passed = models.BooleanField(verbose_name="是否审核通过", default=False)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=255, default='', verbose_name='文章标题')
    short_name = models.CharField(max_length=255, default='', verbose_name='地址显示')
    content = UEditorField(verbose_name='文章内容', width=850, height=400, imagePath="article/ueditor/",
                           filePath="article/ueditor/", default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'articles'
        verbose_name = '文章撰写'
        verbose_name_plural = verbose_name


class ArticleReview(Article):
    """
    在 xadmin 中注册不同数据；
    文章审核
    """
    class Meta:
        verbose_name = '文章审核'
        verbose_name_plural = verbose_name
        proxy = True

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='https://www.baidu.com'>查看</a>")

    go_to.short_description = "查看"


class ArticleApproved(Article):
    """
    在 xadmin 中注册不同数据；
    文章审核通过
    """
    class Meta:
        verbose_name = '已审核文章'
        verbose_name_plural = verbose_name
        proxy = True

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>查看</a>")
    go_to.short_description = "查看"
