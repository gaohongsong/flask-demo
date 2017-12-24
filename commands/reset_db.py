# -*- coding: utf-8 -*-
from flask import current_app
from models import db


def command():
    """initial the database."""

    with current_app.app_context():
        print '[%s]: <reset db>' % current_app
        db.drop_all()
        db.create_all()


command.name = 'reset_db'
