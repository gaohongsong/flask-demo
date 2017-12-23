# -*- coding: utf-8 -*-
from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

from common.http import JsonResponse
from common.converters import ListConverter
from common import factory

# from blueprints import login, error, api, test

app = Flask(__name__, template_folder='templates', static_folder='static')

# load config file from config.py first
app.config.from_object('config')

# return json response
app.response_class = JsonResponse

# register a new converter
app.url_map.converters.update(list=ListConverter)

# setup logfile
factory.add_file_logger(app, 'flask.log')

# register blueprints's blueprint, named by 'bp'
# app.register_blueprint(api.bp)
factory.register_blueprints(app, 'blueprints')


@app.route('/')
def index():
    app.logger.info('test only.')
    return render_template('index.html', **{
        'title': u"标题",
        'name': 'pitou',
    })


if __name__ == '__main__':
    print 'start app: %s' % __name__

    with app.test_request_context():
        print url_for('index')
        print url_for('test.about')
        print url_for('test.user', username='123')
        print url_for('auth.login')
        print url_for('api.list', names=[123, 456], key1='value1')
        print url_for('static', filename='css/index.css')
        print url_for('static', filename='js/index.js')

    app.run(host='0.0.0.0', port=5000, debug=app.debug)
