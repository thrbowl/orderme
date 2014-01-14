from flask import Blueprint, render_template, url_for, current_app

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')


@auth.route('/logout', methods=['POST'])
def logout():
    pass