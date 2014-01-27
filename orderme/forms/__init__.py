from flask.ext.wtf import Form
from wtforms import BooleanField, DateField, FloatField, StringField, IntegerField, DateTimeField, validators
from ..models import Gender


class RegistrationForm(Form):
    username = StringField(validators=[validators.Required(), validators.Length(min=6, max=32)])
    password = StringField(validators=[validators.Required(), validators.Length(min=6, max=32)])
    password_confirm = StringField(validators=[validators.Required(), validators.EqualTo('password')])
    name = StringField(validators=[validators.Optional(), validators.Length(min=2, max=32)])
    gender = IntegerField(validators=[validators.Optional(), validators.AnyOf([Gender.MALE, Gender.FEMALE])])
    birthday = DateField(validators=[validators.Optional(), validators.DataRequired()])
    mobile = StringField(validators=[validators.Required(), validators.Length(min=11, max=11)])
    address = StringField(validators=[validators.Required(), validators.Length(min=10, max=255)])


class LoginForm(Form):
    username = StringField(validators=[validators.Required()])
    password = StringField(validators=[validators.Required()])
    remember = BooleanField()