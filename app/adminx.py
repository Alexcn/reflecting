# -*- coding: utf-8 -*-

import xadmin
from .models import Article
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客系统"
    site_footer = "博客系统"


class ArticleAdmin(object):
    list_display = ['title', 'short_name']
    search_fields = ['title', 'short_name']
    list_filter = ['title', 'short_name']
    model_icon = 'fa fa-eyedropper'
    style_fields = {"content": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
