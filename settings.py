# -*- coding: utf-8 -*-
"""
    settings = conf.default.py + settings_{env}.py
"""
# import os
# import importlib
from conf.default import *

# ========================================================================================
#                               IMPORT ENV SETTINGS
# ========================================================================================

APP_ENV = os.environ.get('APP_ENV', 'develop')
conf_mod = 'conf.settings_{APP_ENV}'.format(APP_ENV=APP_ENV)

try:
    print 'import %s' % conf_mod
    mod = __import__(conf_mod, globals(), locals(), ["*"])
    # mod = importlib.import_module(conf_module)
except ImportError as e:
    raise ImportError("Could not import module '{}': {}".format(conf_mod, e))

# Overwrite upper keys
for setting in dir(mod):
    if setting == setting.upper():
        locals()[setting] = getattr(mod, setting)

# ========================================================================================
#                               FLASK-SQLALCHEMY
# ========================================================================================
DATABASE = DATABASES['default']
if DATABASE['ENGINE'] == 'sqlite':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{NAME}'.format(**DATABASE)
else:
    SQLALCHEMY_DATABASE_URI = 'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DATABASE)