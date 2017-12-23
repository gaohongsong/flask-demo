# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

name = ''
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


