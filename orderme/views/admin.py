# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session, redirect, flash
from flask.ext.login import login_required, login_user, logout_user
from sqlalchemy.orm.exc import NoResultFound
from ..models import *

admin = Blueprint('admin', __name__)

@admin.route('/users', methods=['GET'])
def users():
    user_list = User.query.all()
    return render_template('admin/users.html', has_navbar_cart=False, user_list=user_list)


@admin.route('/goods', methods=['GET'])
def goods():
    goods_list = Goods.query.all()
    return render_template('admin/goods.html', has_navbar_cart=False, goods_list=goods_list)


@admin.route('/orders', methods=['GET'])
def orders():
    orders_list = Order.query.all()
    return render_template('admin/orders.html', has_navbar_cart=False, orders_list=orders_list)