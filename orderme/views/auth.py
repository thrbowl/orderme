from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session, redirect
from flask.ext.login import login_required, login_user, logout_user
from sqlalchemy.orm.exc import NoResultFound
from ..forms import RegistrationForm, LoginForm
from ..models import db, User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        try:
            u = User.query.filter(User.username==form.username,
                                    User.password==form.password).one()
            login_user(u)
        except NoResultFound:
            pass
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(**form.data)
        db.session.add(user)
    return render_template('auth/register.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))