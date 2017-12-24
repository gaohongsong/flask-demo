# -*- coding: utf-8 -*-
"""
    App Factory
    remark: copy from flaskr demo in flask/examples
"""

from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from common import ext
from common.http import JsonResponse
from common.converters import ListConverter
from common.database import db
from models import *

def create_app():

    # app = Flask('flaskr')

    app = Flask(__name__, template_folder='templates', static_folder='static')

    # load config file from settings.py first
    app.config.from_object('settings')

    # return json response
    app.response_class = JsonResponse

    # register a new converter
    app.url_map.converters.update(list=ListConverter)

    # register blueprints's blueprint, named by 'bp'
    ext.register_blueprints(app, 'blueprints')

    # register extra commands
    ext.register_commands(app, 'commands')

    # register context processor
    ext.register_context_processor(app, {
        'test': 'test<script>alert(1)</script>'
    })

    # logger to file
    ext.init_logger(app, 'flask.log')

    # bind db to app
    db.init_app(app)

    # Flask-Migrate
    migrate = Migrate(app, db)

    # Flask-Admin
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Address, db.session))
    admin.add_view(ModelView(Category, db.session))

    return app
