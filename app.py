# -*- coding: utf-8 -*-
import os
from flask import Flask, url_for, make_response
from flask import request, render_template
from flask import redirect, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def debug_request():
    print request.args, request.form, request.is_json


@app.route('/')
def index():
    debug_request()
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })


# 访问 /about/ 404
@app.route('/about')
def about():
    # 1/0
    return redirect(url_for('index'))


# 访问/user/1 重定向到 /user/1/
@app.route('/user/<username>/')
def user(username):
    return 'username: %s' % username


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    debug_request()
    f = request.files['the_file']
    filename = '%s_upload' % secure_filename(f.filename)
    f.save(os.path.join(BASE_DIR, filename))

    return 'post_id: %s' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login: post'
    return 'login: get'


@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    str = ''
    for k, v in request.cookies.iteritems():
        str += '%s: %s | ' % (k, v)
    resp = make_response('cookies: \n%s' % str)

    resp.set_cookie('hello', 'world')
    return resp


# 代码自动重载，500错误时支持在页面调试 Werkzeug
# app.debug = True

if __name__ == '__main__':
    print 'start app: %s' % __name__
    with app.test_request_context():
        print url_for('index')
        print url_for('about')
        print url_for('user', username='123')
        print url_for('static', filename='css/index.css')
        print url_for('static', filename='js/index.js')
    app.run(debug=True)
