# -*- coding: utf-8 -*-

import xadmin
from .models import Author, Tag, Post, Page, Visitor
from xadmin import views


# 审核 <i class="fa fa-eye" aria-hidden="true"></i>
# 评论 <i class="fa fa-comments" aria-hidden="true"></i>
# 

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "GeekTop博客系统"
    site_footer = "GeekTop博客系统"


class AuthorAdmin(object):
    list_display = ['user', 'avatar', 'about']
    search_fields = ['user', 'about']
    list_filter = ['user', 'about']
    model_icon = 'fa fa-user-circle-o'


class TagAdmin(object):
    list_display = ['title', 'slug']
    search_fields = ['title', 'slug']
    list_filter = ['title', 'slug']
    model_icon = 'fa fa-tags'


class PostAdmin(object):
    list_display = ['title', 'author', 'slug', 'publish']
    search_fields = ['author', 'title', 'slug']
    list_filter = ['author', 'title']
    list_editable = ['publish']
    model_icon = 'fa fa-book'

    style_fields = {"description": "ueditor"}


class PageAdmin(object):
    list_display = ['title', 'author', 'slug', 'publish']
    search_fields = ['author', 'title', 'slug']
    list_filter = ['author', 'title']
    list_editable = ['publish']
    model_icon = 'fa fa-files-o'

    style_fields = {"description": "ueditor"}


# class GalleryAdmin(object):
#     list_display = ['title']
#     search_fields = ['title']
#     list_filter = ['title']
#     model_icon = 'fa fa-eyedropper'


class VisitorAdmin(object):
    list_display = ['post', 'ip', 'real_location', 'created']
    list_filter = ['post', 'ip']
    search_fields = ['post', 'ip']
    model_icon = ['post', 'ip']
    # list_editable = ['post', 'ip']
    model_icon = 'fa fa-address-book-o'


xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Page, PageAdmin)
# xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(Visitor, VisitorAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
