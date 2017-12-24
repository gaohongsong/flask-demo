# -*- coding: utf-8 -*-
"""
    App Factory
    remark: copy from flaskr demo in flask/examples
"""

import os

from flask import Flask
from common import app_ext


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

    app_ext.register_blueprints(app, '')
    app_ext.register_cli(app, '', '')
    app_ext.register_teardowns(app, '')

    return app
