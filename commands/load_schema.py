# -*- coding: utf-8 -*-
from models import db


def command():
    """initial the database."""
    with open('schema.sql', 'r') as schema:
        connection = db.engine.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.executescript(schema.read())
            cursor.close()
        finally:
            connection.close()


command.name = 'load_schema'
