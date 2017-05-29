# -*- coding: utf-8 -*-

import xadmin
from .models import Author, Tag, Post, Page, Gallery, Visitor
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "张志亮的博客系统"
    site_footer = "张志亮的博客系统"


class AuthorAdmin(object):
    list_display = ['user', 'avatar', 'about', 'website']
    search_fields = ['user', 'about']
    list_filter = ['user', 'about']
    model_icon = 'fa fa-eyedropper'


class TagAdmin(object):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']
    list_filter = ['title', 'slug']
    model_icon = 'fa fa-eyedropper'


class PostAdmin(object):
    list_display = ['author', 'title', 'slug', 'tags', 'publish']
    search_fields = ['author', 'title', 'slug']
    list_filter = ['author', 'title']
    model_icon = 'fa fa-eyedropper'

    style_fields = {"content": "ueditor"}


class PageAdmin(object):
    list_display = ['author', 'title', 'slug', 'content', 'publish']
    search_fields = ['author', 'title', 'slug']
    list_filter = ['author', 'title']
    model_icon = 'fa fa-eyedropper'

    style_fields = {"content": "ueditor"}


class GalleryAdmin(object):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']
    model_icon = 'fa fa-eyedropper'


class VisitorAdmin(object):
    list_filter = ['post', 'ip']
    search_fields = ['post', 'ip']
    list_filter = ['post', 'ip']
    model_icon = ['post', 'ip']


class ArticleReviewAdmin(object):
    list_display = ['title', 'passed', 'created_at', 'updated_at', 'go_to']
    search_fields = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    model_icon = 'fa fa-graduation-cap'
    list_editable = ['passed']

    style_fields = {"content": "ueditor"}

    # 对菜单的列表页面数据进行过滤；
    def queryset(self):
        qs = super(ArticleReviewAdmin, self).queryset()
        qs = qs.filter(passed=False)
        return qs


class ArticleApprovedAdmin(object):
    list_display = ['title', 'passed', 'created_at', 'updated_at', 'go_to']
    search_fields = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    model_icon = 'fa fa-paper-plane'
    list_editable = ['passed']

    style_fields = {"content": "ueditor"}

    # 对菜单的列表页面数据进行过滤；
    def queryset(self):
        qs = super(ArticleApprovedAdmin, self).queryset()
        qs = qs.filter(passed=True)
        return qs


xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Page, PageAdmin)
xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Visitor, VisitorAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
