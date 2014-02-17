# -*- coding: utf-8 -*-
import datetime
from flask import current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Text, Date, DateTime, func, and_, select
from sqlalchemy.orm import relationship, backref, object_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy(current_app)


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(32), nullable=False)
    name = Column(String(32))
    birthday = Column(Date)
    mobile = Column(String(11), nullable=False)
    address = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False, default=0)
    create_time = Column(DateTime, nullable=False)
    login_time = Column(DateTime, nullable=False)
    _is_active = Column('is_active', Boolean, nullable=True, default=True)

    def __init__(self, **options):
        self.username = options['username']
        self.password = options['password']
        self.name = options.get('name')
        self.mobile = options['mobile']
        self.address = options['address']
        self.create_time = self.login_time = datetime.datetime.now()
        self._is_active = True

        birthday = options.get('birthday')
        birthday_year = options.get('birthday_year')
        birthday_month = options.get('birthday_month')
        birthday_day = options.get('birthday_day')
        if birthday:
            self.birthday = birthday
        elif birthday_year and birthday_month and birthday_day:
            self.birthday = datetime.date(birthday_year, birthday_month, birthday_day)
        else:
            self.birthday = datetime.date.today()

    def is_active(self):
        return self._is_active


class Goods(db.Model):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    create_time = Column(DateTime, nullable=False)
    type = Column(Integer, default=0)
    is_sell = Column(Boolean, nullable=False, default=False)

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
    goods_id = Column(Integer, nullable=False)
    goods_num = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.package_id = options['package_id']
        self.goods_id = options['goods_id']
        self.goods_num = options['goods_num']


class OrderStatus(object):
    NEW = 1
    SEND = 2
    SIGN = 3
    PAY = 4


class Order(db.Model):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    mobile = Column(String(11), nullable=False)
    address = Column(String(255), nullable=False)
    cost = Column(Float, nullable=False, default=0)
    create_time = Column(DateTime, nullable=False)
    send_time = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.name = options['name']
        self.mobile = options['mobile']
        self.address = options['address']
        self.cost = options['cost']
        self.create_time = datetime.datetime.now()
        self.send_time = options['send_time']
        self.status = OrderStatus.NEW


class OrderDetail(db.Model):
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True)
    goods_id = Column(Integer, nullable=False)
    num = Column(Integer, nullable=False)

    def __init__(self, **options):
        self.order_id = options['order_id']
        self.goods_id = options['goods_id']
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
