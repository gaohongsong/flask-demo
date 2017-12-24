# -*- coding: utf-8 -*-
from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

from factory import create_app

app = create_app()

# test only
with app.test_request_context():
    print url_for('root.index')
    print url_for('api.list', names=[123, 456], key1='value1')
    print url_for('auth.login')
    print url_for('test.about')
    print url_for('test.user', username='123')
    print url_for('static', filename='css/index.css')
    print url_for('static', filename='js/index.js')

if __name__ == '__main__':
    app.run()
    # flask run -h 0.0.0.0 -p 5000 --debugger --reload
    # app.run(host='0.0.0.0', port=5000, debug=app.debug)
