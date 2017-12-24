# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

from common.cache import simple_cache

name = 'root'
bp = Blueprint(name, __name__, url_prefix='/')


@simple_cache.cached(timeout=50, key_prefix='all_comments')
def get_all_comments():
    print 'get_all_comments'
    comments = range(1000)
    return comments


@bp.route('/')
@simple_cache.cached(timeout=50)
def index():
    # test only
    current_app.logger.info('test only.')
    cached_comments = get_all_comments()
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })
