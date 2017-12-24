# -*- coding: utf-8 -*-
import sqlite3

from flask import current_app, g


def command():
    """initial the database."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(current_app.config['DATABASE'])
        g.sqlite_db.row_factory = sqlite3.Row

    with current_app.open_resource('schema.sql', mode='r') as f:
        g.sqlite_db.cursor().executescript(f.read())
    g.sqlite_db.commit()


command.name = 'init_db'
