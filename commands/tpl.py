# -*- coding: utf-8 -*-
from flask import current_app, g


def command():
    """flask tpl"""
    print '%s: do something' % current_app


command.name = 'tpl'
