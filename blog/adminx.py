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

    style_fields = {"description": "ueditor"}


class PageAdmin(object):
    list_display = ['author', 'title', 'slug', 'publish']
    search_fields = ['author', 'title', 'slug']
    list_filter = ['author', 'title']
    model_icon = 'fa fa-eyedropper'

    style_fields = {"description": "ueditor"}


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


xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Page, PageAdmin)
xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Visitor, VisitorAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
