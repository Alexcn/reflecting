
from flask.ext.wtf import Form
from wtfroms import StringField, BooleadField
from wtforms.validators import DataRequired


class LoginFrom(Form):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleadField('remember_me', default=False)