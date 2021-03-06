# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, render_template, url_for
from flask.ext.login import LoginManager

try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = '<unknown>'


def create_app(name=None, settings=None):
    """http://flask.pocoo.org/docs/patterns/appfactories/"""
    app = Flask(name or __name__)

    # register settings
    # priority: env variable > params > settings.py
    app.config.from_pyfile('settings.py')
    if settings is not None:
        if isinstance(object, settings):
            app.config.from_object(settings)
        elif os.path.isfile(os.path.join(app.root_path, settings)):
            app.config.from_pyfile(settings)
    app.config.from_envvar('ORDERME_SETTINGS', silent=True)

    logging.debug('add session SECRET_KEY')
    app.secret_key = app.config['SECRET_KEY']

    logging.debug('register blueprints to app')
    with app.app_context():
        from .views.main import main
        app.register_blueprint(main)
        from .views.order import order
        app.register_blueprint(order, url_prefix='/order')
        from .views.auth import auth
        app.register_blueprint(auth, url_prefix='/auth')
        from .views.user import user
        app.register_blueprint(user, url_prefix='/user')
        from .views.cart import cart
        app.register_blueprint(cart, url_prefix='/cart')
        from .views.admin import admin
        app.register_blueprint(admin, url_prefix='/admin')

    logging.debug('add global templates function')
    app.jinja_env.globals['static'] = (lambda filename: url_for('static', filename=filename))

    logging.debug('register error process handlers')
    @app.errorhandler(404)
    def http404(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def http500(error):
        return render_template('500.html'), 500

    logging.debug('add database auto commit callback')
    @app.teardown_request
    def teardown_request(e=None):
        from .models import db
        try:
            if e is None:
                try:
                    db.session.commit()
                except Exception, e:
                    logging.error(str(e))
                    db.session.rollback()
        finally:
            db.session.remove()

    logging.debug('add user login manager')
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def user_loader(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app
