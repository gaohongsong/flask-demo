# -*- coding: utf-8 -*-
from datetime import datetime

from common.database import (db, Model, Column, SurrogatePK,
                             reference_col, relationship)


class Post(SurrogatePK, Model):
    __tablename__ = 'posts'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(80))
    body = Column(db.Text)
    pub_date = Column(db.DateTime)

    category_id = reference_col('category', nullable=True)
    category = relationship('Category', backref='posts')

    # category_id = Column(db.Integer, db.ForeignKey('category.id'))
    # category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title='', body='', category=None, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(SurrogatePK, Model):
    __tablename__ = 'category'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(50))
    desc = Column(db.String(50))

    def __init__(self, name=''):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
