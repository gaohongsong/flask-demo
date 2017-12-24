# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

name = 'root'
bp = Blueprint(name, __name__, url_prefix='/')


@bp.route('/')
def index():
    # test only
    current_app.logger.info('test only.')
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })
