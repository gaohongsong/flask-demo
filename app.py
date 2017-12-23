# -*- coding: utf-8 -*-
import os

from flask import Flask, flash
from flask import request, url_for, session, escape
from flask import redirect, abort, make_response, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# load config file from config.py
app.config.from_object('config')

# logger to local file flask.log
if app.debug is not True:
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler(
        os.path.join(app.config.BASE_DIR, 'flask.log'),
        maxBytes=1024 * 1024 * 100, backupCount=20
    )
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[ %(asctime)s ][ %(levelname)s ][ %(name)s ]: %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)


@app.route('/')
def index():
    app.logger.info('render index template.')
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                        request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


# 访问 /about/ 404
@app.route('/about')
def about():
    return redirect(url_for('index'))


# @app.errorhandler(404)
# def handle_404(error):
#     # response, status, headers
#     return render_template('404.html'), 404

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Custom-Header'] = 'Something'
    return resp


# 访问/user/1 重定向到 /user/1/
@app.route('/user/<username>/')
def user(username):
    return 'username: %s' % username


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    f = request.files['the_file']
    filename = '%s_upload' % secure_filename(f.filename)
    f.save(os.path.join(app.config.BASE_DIR, filename))

    return 'post_id: %s' % post_id


@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    str = ''
    for k, v in request.cookies.iteritems():
        str += '%s: %s | ' % (k, v)
    resp = make_response('cookies: \n%s' % str)

    resp.set_cookie('hello', 'world')
    return resp


if __name__ == '__main__':
    print 'start app: %s' % __name__

    with app.test_request_context():
        print url_for('index')
        print url_for('about')
        print url_for('user', username='123')
        print url_for('static', filename='css/index.css')
        print url_for('static', filename='js/index.js')

    app.run(host='0.0.0.0', port=5000, debug=app.debug)
