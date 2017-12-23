# -*- coding: utf-8 -*-
"""
    App Factory
"""

import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, g
from werkzeug.utils import find_modules, import_string


def create_app(config=None):
    app = Flask('flaskr')

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    register_blueprints(app, '')
    register_cli(app, '')
    register_teardowns(app)

    return app


def register_blueprints(app, bp_pkg):
    """Register all blueprint modules

    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules(bp_pkg):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app, cmd):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        cmd()
        print('Initialized the database.')


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()


def add_file_logger(app, filename):
    """
    log to local file
    """
    file_handler = RotatingFileHandler(
        os.path.join(app.root_path, filename),
        maxBytes=1024 * 1024 * 100, backupCount=20
    )
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[ %(asctime)s ][ %(levelname)s ][ %(name)s ]: %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
