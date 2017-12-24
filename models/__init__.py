# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from common.utils import import_to_context

# global db
db = SQLAlchemy()

# export all models
import_to_context('models', locals())
