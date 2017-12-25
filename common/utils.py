# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""

from flask import flash
from flask_sqlalchemy import DefaultMeta
from werkzeug.utils import find_modules
from importlib import import_module


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)


def import_to_context(pkg, locals_context):
    """
    from pkg import *
    """
    for name in find_modules(pkg):

        mod = import_module(name)

        # import db.Model's Class to locals_context
        for attr in dir(mod):
            mod_attr = getattr(mod, attr)

            # skip
            if not isinstance(mod_attr, DefaultMeta) or attr in locals_context:
                continue

            # import db.Model
            print 'from {} import {}'.format(name, attr)
            locals_context[attr] = getattr(mod, attr)
