# -*- encoding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


# 数据库文件的的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# 存储迁移脚本的目录
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


CSRF_ENABLED = True
SECRET_KEY = 'hv0cOb3jfnsRpYAumjutQfgeD9Cs2vQL'