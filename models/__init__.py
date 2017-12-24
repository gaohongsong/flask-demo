# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy, DefaultMeta
from werkzeug.utils import find_modules
from importlib import import_module

# global db
db = SQLAlchemy()

# export all models
for name in find_modules('models'):
    mod = import_module(name)
    for attr in dir(mod):
        mod_attr = getattr(mod, attr)
        if isinstance(mod_attr, DefaultMeta):
            print 'model import: %s' % attr
            locals()[attr] = getattr(mod, attr)
