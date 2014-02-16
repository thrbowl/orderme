# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session, redirect, flash
from flask.ext.login import login_required, login_user, logout_user
from sqlalchemy.orm.exc import NoResultFound


admin = Blueprint('admin', __name__)

@admin.route('/goods', methods=['GET'])
def goods():
    return render_template('admin/goods.html', has_navbar_cart=False)

@admin.route('/users', methods=['GET'])
def users():
    return render_template('admin/users.html', has_navbar_cart=False)

@admin.route('/orders', methods=['GET'])
def orders():
    return render_template('admin/orders.html', has_navbar_cart=False)