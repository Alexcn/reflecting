from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from DjangoUeditor.models import UEditorField


# from redactor.fields import RedactorField


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(models.Model):
    user = models.ForeignKey(User, related_name='author')
    avatar = models.ImageField(upload_to='gallery/avatar/%Y/%m/%d',
                               null=True,
                               blank=True,
                               help_text="Upload your photo for Avatar")
    about = models.TextField()
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('author_posts_page',
                       kwargs={'username': self.user.username})

    class Meta:
        verbose_name = '作者详情'
        verbose_name_plural = '作者'


class Tag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    @property
    def get_total_posts(self):
        return Post.objects.filter(tags__pk=self.pk).count()

    class Meta:
        verbose_name = '标签详情'
        verbose_name_plural = '标签'


class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Post(TimeStampedModel):
    author = models.ForeignKey(Author, related_name='author_post', verbose_name='文章作者')
    title = models.CharField(max_length=200, verbose_name='文章标题')
    slug = models.SlugField(max_length=200, unique=True)
    cover = models.ImageField(upload_to='gallery/covers/%Y/%m/%d',
                              null=True,
                              blank=True,
                              help_text='Optional cover post')
    # description = RedactorField()
    description = UEditorField(verbose_name='文章内容', width=850, height=400, imagePath="blog/post/",
                               filePath="blog/post/", default='')
    tags = models.ManyToManyField('Tag', verbose_name='文章标签')
    keywords = models.CharField(max_length=200, null=True, blank=True,
                                help_text='Keywords sparate by comma.', verbose_name='文章关键字')
    meta_description = models.TextField(null=True, blank=True, verbose_name='文章描述')

    publish = models.BooleanField(default=False, verbose_name='是否审核通过')
    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('detail_post_page', kwargs={'slug': self.slug})

    @property
    def total_visitors(self):
        return Visitor.objects.filter(post__pk=self.pk).count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = '文章'
        ordering = ["-created"]


class Page(TimeStampedModel):
    author = models.ForeignKey(Author, related_name='author_page')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = UEditorField(verbose_name='页面内容', width=850, height=400, imagePath="blog/page/",
                               filePath="blog/page/", default='')
    publish = models.BooleanField(default=True, verbose_name='是否审核通过')

    def __str__(self):
        return self.title

    # this will be an error in /admin
    # def get_absolute_url(self):
    #    return reverse("page_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "页面详情"
        verbose_name_plural = "页面"
        ordering = ["-created"]


class Gallery(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name='标题')
    attachment = models.FileField(upload_to='gallery/attachment/%Y/%m/%d', verbose_name='上传')

    def __str__(self):
        return self.title

    def check_if_image(self):
        if self.attachment.name.split('.')[-1].lower() in ['jpg', 'jpeg', 'gif', 'png']:
            return '<img height="40" width="60" src="%s"/>' % self.attachment.url
        else:
            return '<img height="40" width="60" src="/static/assets/icons/file-icon.png"/>'

    check_if_image.short_description = 'Attachment'
    check_if_image.allow_tags = True

    class Meta:
        verbose_name = 'Detail Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ['-created']


class Visitor(TimeStampedModel):
    post = models.ForeignKey(Post, related_name='post_visitor')
    ip = models.CharField(max_length=40, verbose_name='访客IP')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = '访客详情'
        verbose_name_plural = '访客'
        ordering = ['-created']
