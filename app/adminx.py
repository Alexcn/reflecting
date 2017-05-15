# -*- coding: utf-8 -*-

import xadmin
from .models import Article
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "FengXiao博客系统"
    site_footer = "FengXiao博客系统"
