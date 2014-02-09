# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template, url_for, current_app, request, g, flash, session, redirect, flash
from flask.ext.login import login_required, login_user, logout_user
from sqlalchemy.orm.exc import NoResultFound


cart = Blueprint('cart', __name__)

@cart.route('/', methods=['GET'])
def index():
    return render_template('cart/index.html')