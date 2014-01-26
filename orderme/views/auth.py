from flask import Blueprint, render_template, url_for, current_app, request
from ..forms import RegistrationForm
from ..models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(form.data)
    return render_template('auth/register.html', form=form)

@auth.route('/logout', methods=['POST'])
def logout():
    pass