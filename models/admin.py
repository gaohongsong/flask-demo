# -*- coding: utf-8 -*-

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models.user import *
from models.blog import *

admin = Admin(name='Flask-Admin', template_mode='bootstrap3')


class PostModelView(ModelView):
    can_delete = False  # disable model deletion
    # can_create = False
    # can_edit = False
    can_view_details = True

    page_size = 50  # the number of entries to display on the list view
    column_exclude_list = ['pub_date', ]
    column_searchable_list = ['title', 'body']
    column_filters = ['title']


admin.add_view(ModelView(User, db.session))
admin.add_view(PostModelView(Post, db.session))
admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Todo, db.session))
