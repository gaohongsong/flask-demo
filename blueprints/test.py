# -*- coding: utf-8 -*-
import os

from werkzeug.utils import secure_filename
from flask import (
    Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app,
    make_response
)

name = 'test'
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


# URL规范：访问 /about/ 404
@bp.route('/about')
def about():
    return redirect(url_for('index'))


# URL规范：访问/user/1 重定向到 /user/1/
@bp.route('/user/<username>/')
def user(username):
    return 'username: %s' % username


# 文件操作
@bp.route('/post/<int:post_id>/', methods=['GET', 'POST'])
def post(post_id):
    f = request.files['the_file']
    filename = '%s_upload' % secure_filename(f.filename)
    f.save(os.path.join(current_app.root_path, filename))

    return 'post_id: %s' % post_id


# 读写cookie
@bp.route('/cookies/', methods=['GET', 'POST'])
def cookies():
    str = ''
    for k, v in request.cookies.iteritems():
        str += '%s: %s | ' % (k, v)
    resp = make_response('cookies: \n%s' % str)

    resp.set_cookie('hello', 'world')
    return resp
