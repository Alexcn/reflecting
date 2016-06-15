# -*- encoding: utf-8 -*-
from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name


# usertype 类型需要外键关联到 roles 表
class User(db.Model):
    __tablename__ = 'users'
    # id = db.Column(db.Sequence, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    usertype = db.Column(db.Integer, db.ForeignKey('roles.id'))
    birthday = db.Column(db.DATE)
    address = db.Column(db.String(256))
    email = db.Column(db.String(64), unique=True)
    phone = db.Column(db.CHAR(16), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Post %r>' % self.title



