# -*- coding: utf-8 -*-
import click
from flask import json, current_app
from flask.cli import with_appcontext

from common.database import db


@click.command()
@with_appcontext
def command():
    """drop tables."""

    print '[%s]: <reset db>' % current_app
    db.drop_all()