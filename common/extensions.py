# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""

from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from common.logger import Logger

admin = Admin(name='Flask-Admin', template_mode='bootstrap3')
logger = Logger()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
debug_toolbar = DebugToolbarExtension()
webpack = Webpack()
