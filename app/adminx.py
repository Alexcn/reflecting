# -*- coding: utf-8 -*-

import xadmin
from .models import Article, ArticleReview, ArticleApproved
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "博客系统"
    site_footer = "博客系统"


class ArticleAdmin(object):
    list_display = ['title', ]
    search_fields = ['title', 'short_name']
    list_filter = ['title', 'short_name']
    model_icon = 'fa fa-eyedropper'
    style_fields = {"content": "ueditor"}


class ArticleReviewAdmin(object):
    list_display = ['title', 'passed', 'created_at', 'updated_at', 'go_to', 'keywords']
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


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(ArticleReview, ArticleReviewAdmin)
xadmin.site.register(ArticleApproved, ArticleApprovedAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
