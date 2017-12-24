# -*- coding: utf-8 -*-
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username='', email=''):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('address', lazy='dynamic'))

    def __init__(self, email_address='', user=None):
        self.email_address = email_address
        self.user = user

    def __repr__(self):
        return '<Adress %r>' % self.email_address
