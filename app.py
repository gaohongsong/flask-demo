# -*- coding: utf-8 -*-
from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

from common.http import JsonResponse
from common.converters import ListConverter
from common import app_ext
from models import db

app = Flask(__name__, template_folder='templates', static_folder='static')

# load config file from config.py first
app.config.from_object('config')
# load config from env settings
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# return json response
app.response_class = JsonResponse

# register a new converter
app.url_map.converters.update(list=ListConverter)

# register blueprints's blueprint, named by 'bp'
app_ext.register_blueprints(app, 'blueprints')

# register extra commands
app_ext.register_commands(app, 'commands')

# register context processor
app_ext.register_context_processor(app, {
    'test': 'test<script>alert(1)</script>'
})

# logger init
app_ext.init_logger(app, 'flask.log')

# db init
db.init_app(app)


def debug_context():
    """app.teardown_appcontext"""
    if app.debug:
        app.logger.info('before response hook')


# register app context
app_ext.register_teardowns(app, debug_context)


@app.before_request
def debug_request():
    """app.before_request"""
    if app.debug:
        print '''
            method: {}
            url: {}
            headers: {}
            args: {}
            form: {}
            cookies: {}
        '''.format(
            request.method,
            request.url,
            request.headers,
            request.args,
            request.form,
            request.cookies
        )


@app.route('/')
def index():
    # test only
    app.logger.info('test only.')
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })


# test only
with app.test_request_context():
    print url_for('index')
    print url_for('test.about')
    print url_for('test.user', username='123')
    print url_for('auth.login')
    print url_for('api.list', names=[123, 456], key1='value1')
    print url_for('static', filename='css/index.css')
    print url_for('static', filename='js/index.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.debug)
