# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.user import *
from models.blog import *

admin = Admin(name='Flask-Admin', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Todo, db.session))
