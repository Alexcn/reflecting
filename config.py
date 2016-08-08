# -*- encoding: utf-8 -*-

import os
from yaml import load

try:
    from yaml import CLoader as Loader
except:
    from yaml import Loader

db_config_stream = open('./config/database.yml', 'r')
db_config = load(db_config_stream, Loader=Loader)
db_config_stream.close()

print(db_config['development']['database'])

basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'hv0cOb3jfnsRpYAumjutQfgeD9Cs2vQL'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or SECRET_KEY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[reflecting]'
    FLASKY_MAIL_SENDER = 'reflecting Admin <admin@itpub.me>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@{host}:{port}/{dbname}'.format(
        username=db_config['development']['username'],
        password=db_config['development']['password'],
        host=db_config['development']['host'],
        port=db_config['development']['port'],
        dbname=db_config['development']['database'],
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = None


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = None


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}