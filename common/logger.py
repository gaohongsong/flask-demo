# -*- coding: utf-8 -*-
"""
    App Factory
"""

import os
import logging
from logging.handlers import RotatingFileHandler


class Logger(object):
    def __init__(self, app=None, filename=None, format=None, level=logging.INFO, **kwargs):
        self.filename = filename or 'app.log'
        self.format = format or "[ %(asctime)s ][ %(levelname)s ][ %(name)s ]: %(message)s"
        self.level = level
        self.app = app

        if self.app is not None:
            self.init_app(app, filename)

    def init_app(self, app, filename=None, **kwargs):
        self.filename = filename or self.filename

        file_handler = RotatingFileHandler(
            os.path.join(app.root_path, filename),
            maxBytes=1024 * 1024 * 100, backupCount=20
        )
        file_handler.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

        return app.logger
