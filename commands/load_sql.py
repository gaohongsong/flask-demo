# -*- coding: utf-8 -*-
import click
from flask import json
from flask.cli import with_appcontext
from common.database import db


@click.command()
@click.option('--file', default='schema.sql',
              help='Sql File To Load (ex. /static/image.png)')
def command(file):
    """initial the database."""
    print file
    # with open(file, 'r') as schema:
    #     connection = db.engine.raw_connection()
    #     try:
    #         cursor = connection.cursor()
    #         cursor.executescript(schema.read())
    #         cursor.close()
    #     finally:
    #         connection.close()
