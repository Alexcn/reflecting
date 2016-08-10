# -*- encoding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('登录')


class RegistrationFrom(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          '用户名只能由字母、数字、下划线和点组成')])
    password = PasswordField('输入密码', validators=[Required(),
                                                 EqualTo('password2', message='两次输入密码不匹配')])
    password2 = PasswordField('再次输入密码', validators=[Required])
    submit = SubmitField('提交')

    def validate_email(self, field):
        '''field 由外部传入'''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('改邮箱已经被注册')

    def validate_username(self, filed):
        if User.query.filter_by(usernem=filed.data).first():
            raise ValidationError('用户名已经被使用')