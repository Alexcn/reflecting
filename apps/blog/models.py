from django.db import models

# Create your models here.

__all__ = [
    'Categories',
    'Article',
    'Link',
    'Tag',
    'Setting'
]


class Categories(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def categories_article_count(self):
        return self.article_set.all().count()


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def tag_article_count(self):
        return self.article_set.all().count()


class Article(models.Model):
    STATUS_CHOICES = (
        ('0', '发布'),
        ('1', '存稿'),
    )

    title = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    release_time = models.DateTimeField(default='1970-1-1 00:00:00')
    status = models.CharField(default=0, max_length=1, choices=STATUS_CHOICES)
    read = models.IntegerField(default=0)
    categories = models.ManyToManyField(Categories)
    tag = models.ManyToManyField(Tag)

    def get_categories(self):
        categories = ''
        for c in self.categories.all():
            categories += ',' + c.name
        return categories.strip(',')

    def get_tag(self):
        tag = ''
        for t in self.tag.all():
            tag += ',' + t.name
        return tag.strip(',')

    def get_comment_num(self):
        from users.models import Comment
        return Comment.objects.filter(article=self.id).count()

    def get_tags(self):
        return Tag.objects.filter(article=self.pk)


class Link(models.Model):
    name = models.CharField(max_length=32, unique=True)
    url = models.URLField(unique=True)
    description = models.CharField(max_length=255, default='此用户没有添加任何描述')
    add_time = models.DateTimeField(auto_now_add=True)


class Setting(models.Model):
    title = models.CharField(max_length=80)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='%Y/%m', max_length=100)
    homedescription = models.CharField(max_length=150)
    recordinfo = models.CharField(max_length=100)
    statisticalcode = models.TextField()
