# -*- coding: utf-8 -*-
"""
    App Factory
"""

import os
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.utils import find_modules, import_string


def register_blueprints(app, bp_pkg):
    """register all blueprint modules in bp_pkg package
    """
    for name in find_modules(bp_pkg):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_commands(app, cli_pkg):
    for name in find_modules(cli_pkg):
        mod = import_string(name)
        if hasattr(mod, 'command'):
            print '[register-cli]: <%s>' % mod.command.name
            register_cli(app, mod.command)
    return None


def register_cli(app, func):
    @app.cli.command(func.name)
    def command():
        """execute cmd_func."""
        func()


def register_teardowns(app, func):
    @app.teardown_appcontext
    def command(error):
        func()


def register_context_processor(app, extra_context):
    @app.context_processor
    def context():
        return extra_context


def init_logger(app, filename):
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

    return app.logger
