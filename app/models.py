# -*- encoding: utf-8 -*-

from . import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    phone_num = db.Column(db.BigInteger, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.username


class UserLog(db.Model):
    __tablename__ = 'user_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('user_logs', lazy='dynamic'))
    ip = db.Column(db.String)
    access_time = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return '<access_ip %r>' % self.ip


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, Comment='文章的标题')
    content = db.Column(db.Text, Comment='文章的内容')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), Comment='文章作者的ID')
    created_at = db.Column(db.TIMESTAMP, Comment='文章创建的时间')
    updated_at = db.Column(db.TIMESTAMP, Comment='文章最近一次修改的时间')
    status = db.Column(db.SMALLINT, Comment='1: 发表; 2: 草稿; 3: 审核; 4: 删除')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('users', lazy='dynamic'))


class Article_modify_version(db.Model):
    __tablename__ = 'article_modify_versions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    user = db.relationship('User', backref=db.backref('article_modify_versions', lazy='dynamic'))
    article = db.relationship('Article', backref=db.backref('article_modify_versions', lazy='dynamic'))
    created_time = db.Column(db.TIMESTAMP)





