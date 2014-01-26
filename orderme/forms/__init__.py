from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, FloatField, IntegerField, validators
from ..models import Gender


class RegistrationForm(Form):
    username = TextField('username', [validators.Required(), validators.Length(min=6, max=32)])
    password = PasswordField('password', [validators.Required(), validators.Length(min=6, max=32)])
    password_confirm = PasswordField('password_confirm', [validators.Required(), validators.EqualTo('password_confirm')])
    name = TextField('name', [validators.Length(min=2, max=32)])
    gender = IntegerField(validators=[validators.AnyOf([Gender.MALE, Gender.FEMALE])])
    birthday = TextField('birthday')
    mobile = TextField('mobile', [validators.Required(), validators.Length(min=11, max=11)])
    address = TextField('address', [validators.Length(min=10, max=255)])


class LoginForm(Form):
    pass