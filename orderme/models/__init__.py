import datetime
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Text, Date, DateTime, func, and_, select
from sqlalchemy.orm import relationship, backref, object_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy(current_app)


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False)
    password = Column(String(32), nullable=False)
    name = Column(String(32))
    gender = Column(Integer, default=0)
    birthday = Column(Date)
    mobile = Column(String(11), nullable=False)
    cost = Column(Float, nullable=False, default=0)
    create_time = Column(DateTime)
    login_time = Column(DateTime)

    def __init__(self, **options):
        self.username = options['username']
        self.password = options['password']
        self.name = options.get('name')
        self.gender = options.get('name')
        self.birthday = options.get('birthday')
        self.mobile = options['mobile']
        self.create_time = self.login_time = datetime.datetime.now()


"""
class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

    def __init__(self, **options):
        self.name = options['name']
        self.price = options['price']
        self.description = options.get('description')


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
"""