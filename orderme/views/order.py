from flask import Blueprint, render_template, url_for, current_app

order = Blueprint('order', __name__)


@order.route('/', methods=['GET'])
def index():
    pass