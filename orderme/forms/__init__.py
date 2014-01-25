from wtforms import Form, BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
    username = TextField('username', [validators.Required(), validators.Length(min=6, max=32)])
    password = PasswordField('password', [validators.Required(), validators.Length(min=6, max=32)])
    password_confirm = PasswordField('password_confirm', [validators.Required(), validators.EqualTo('password_confirm')])
    name = TextField('name', [validators.Length(min=2, max=32)])
