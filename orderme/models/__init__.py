import datetime
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean, Text, DateTime, func, and_, select
from sqlalchemy.orm import relationship, backref, object_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy(current_app)


class User(db.Model):
    def __init__(self, username, password, **options):
        self.username = username
        self.password = password
        self.name = options.get('name')
        self.birthday = options.get('birthday')
        self.phone = options.get('phone')
        self.address = options.get('address')

    def cost(self):
        pass

class Product(db.Model):
    def __init__(self, name, price, **options):
        self.name = name
        self.price = price
        self.description = options.get('description')
        self.pergroup = options.get('pergroup')

class Order(db.Model):
    def __init__(self, name, phone, address, cost, **options):
        self.name = name
        self.phone = phone
        self.address = address
        self.cost = cost
        self.user_id = options.get('user_id')
        self.order_time = datetime.datetime.now()
        self.send_time = options.get('send_time', self.order_time)

class OrderProduct(db.Model):
    def __init__(self, order_id, product_id, amount, cost):
        self.order_id = order_id
        self.product_id = product_id
        self.amount = amount
        self.cost = cost

class SystemConfig(db.Model):
    pass