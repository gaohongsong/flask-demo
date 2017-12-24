# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from common.utils import import_to_context

# global db
db = SQLAlchemy()

# export all models
import_to_context('models', locals())

# Flask-Migrate
migrate = Migrate()
