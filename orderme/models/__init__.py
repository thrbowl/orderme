import datetime
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Text, Date, DateTime, func, and_, select
from sqlalchemy.orm import relationship, backref, object_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy(current_app)


class Gender(object):
    MALE = 1
    FEMALE = 2


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
    create_time = Column(DateTime, nullable=False)
    login_time = Column(DateTime, nullable=False)

    def __init__(self, **options):
        self.username = options['username']
        self.password = options['password']
        self.name = options.get('name')
        self.gender = options.get('gender')
        self.birthday = options.get('birthday')
        self.mobile = options['mobile']
        self.create_time = self.login_time = datetime.datetime.now()


class Address(db.Model):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)

    def __init__(self, user_id, address):
        self.user_id = user_id
        self.address = address


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    create_time = Column(DateTime, nullable=False)
    is_sell = Column(Boolean, nullable=False)

    def __init__(self, **options):
        self.name = options['name']
        self.price = options['price']
        self.description = options.get('description')
        self.create_time = datetime.datetime.now()
        self.is_sell = False


class PackageDetail(db.Model):
    __tablename__ = 'package_detail'

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    product_num = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.package_id = options['package_id']
        self.product_id = options['product_id']
        self.product_num = options['product_num']


class OrderStatus(object):
    NEW = 1
    SEND = 2
    SIGN = 3
    PAY = 4


class Order(db.Model):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    mobile = Column(String(11), nullable=False)
    address = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False, default=0)
    create_time = Column(DateTime, nullable=False)
    send_time = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.mobile = options['mobile']
        self.address = options['address']
        self.cost = options['cost']
        self.create_time = datetime.datetime.now()
        self.send_time = options['send_time']
        self.status = OrderStatus.NEW


class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, nullable=False)
    num = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.order_id = options['order_id']
        self.product_id = options['product_id']
        self.num = options['num']


#class SystemConfig(db.Model):
#    __tablename__ = 'system_config'
#
#
#class Notice(db.Model):
#    __tablename__ = 'notice'
#
#    id = Column(Integer, primary_key=True)
#    title = Column(String(255), nullable=False)
#    content = Column(Text, nullable=False)
#
#    def __init__(self, **options):
#        self.title = options['title']
#        self.content = options['content']
