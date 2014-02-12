# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session, redirect
from flask.ext.login import login_required, login_user, logout_user, current_user
from sqlalchemy.orm.exc import NoResultFound
from ..forms import RegistrationForm, LoginForm
from ..models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/check/username_unique', methods=['GET'])
def check_username_unique():
    username = request.args['username']
    try:
        user = User.query.filter(User.username == username).one()
        ret = False
    except NoResultFound:
        ret = True
    return json.dumps(ret)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User(**form.data)
        db.session.add(user)
        db.session.flush()
        flash(u'您的帐户%s已注册成功' % user.username, 'info')
        login_user(user)
        return redirect(url_for('main.home'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        try:
            u = User.query.filter(User.username == form.username.data,
                User.password == form.password.data).one()
            login_user(u, remember=form.remember.data)
        except NoResultFound:
            pass
    return redirect(url_for('main.home'))


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))