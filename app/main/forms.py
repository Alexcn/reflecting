# -*- encoding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField('请输入你的名字', validators=[Required()])
    submit = SubmitField('提交')


class ArticleForm(Form):
    title = StringField('标题', validators=[Required()])
    body = PageDownField(validators=[Required()])
    submit = SubmitField('提交')


class CommentForm(Form):
    body = SubmitField('请输入评论的内容', validators=[Required()])
    submit = SubmitField('提交')
