# -*- encoding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('请输入你的名字', validators=[Required()])
    submit = SubmitField('提交')