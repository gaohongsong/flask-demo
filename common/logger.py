# -*- coding: utf-8 -*-

import os
import logging
from logging.handlers import RotatingFileHandler


def setup(app, filename):
    """
    log to local file
    """
    file_handler = RotatingFileHandler(
        os.path.join(app.config['BASE_DIR'], filename),
        maxBytes=1024 * 1024 * 100, backupCount=20
    )
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[ %(asctime)s ][ %(levelname)s ][ %(name)s ]: %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
