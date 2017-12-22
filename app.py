# -*- coding: utf-8 -*-

from flask import Flask, url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    # 1/0
    return 'index'


# 访问 /about/ 404
@app.route('/about')
def about():
    return 'about'


# 访问/user/1 重定向到 /user/1/
@app.route('/user/<username>/')
def user(username):
    return 'username: %s' % username


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'post_id: %s' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login: post'
    return 'login: get'


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
