# coding: utf-8
"""
    pip install flask-sqlacodegen
    https://github.com/ksindi/flask-sqlacodegen
    flask-sqlacodegen.exe --flask mysql://root:root@localhost:3306/flask  --outfile sqlacodegen_tables.py
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Addres(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(80))
    user_id = db.Column(db.ForeignKey(u'user.id'), index=True)

    user = db.relationship(u'User', primaryjoin='Addres.user_id == User.id', backref=u'address')


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    category_id = db.Column(db.ForeignKey(u'category.id'), index=True)

    category = db.relationship(u'Category', primaryjoin='Post.category_id == Category.id', backref=u'posts')


class Todo(db.Model):
    __tablename__ = 'todos'

    todo_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.Text)
    done = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
