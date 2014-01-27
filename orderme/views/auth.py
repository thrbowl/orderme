from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session
from ..forms import RegistrationForm, LoginForm
from ..models import db, User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(**form.data)
        db.session.add(user)
    return render_template('auth/register.html', form=form)

@auth.route('/logout', methods=['POST'])
def logout():
    pass