# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import BooleanField, DateField, FloatField, StringField, IntegerField, DateTimeField, validators


class RegistrationForm(Form):
    username = StringField(validators=[validators.Required(), validators.Length(min=6, max=32)])
    password = StringField(validators=[validators.Required(), validators.Length(min=6, max=32)])
    password_confirm = StringField(validators=[validators.Required(), validators.EqualTo('password')])
    name = StringField(validators=[validators.Required(), validators.Length(min=2, max=32)])
    birthday_year = IntegerField(validators=[validators.Optional()])
    birthday_month = IntegerField(validators=[validators.Optional()])
    birthday_day = IntegerField(validators=[validators.Optional()])
    mobile = StringField(validators=[validators.Required(), validators.Length(min=11, max=11)])
    address = StringField(validators=[validators.Required(), validators.Length(min=7, max=255)])


class LoginForm(Form):
    username = StringField(validators=[validators.Required()])
    password = StringField(validators=[validators.Required()])
    remember = BooleanField()