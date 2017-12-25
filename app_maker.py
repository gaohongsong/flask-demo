# -*- coding: utf-8 -*-
"""
    App Factory
    remark: copy from flaskr demo in flask/examples
"""

from flask import Flask, render_template
from werkzeug.utils import find_modules, import_string

from common.http import JsonResponse
from common.converters import ListConverter
from common.extensions import (cache, db, logger, migrate,
                               bcrypt, csrf_protect, login_manager,
                               debug_toolbar, webpack)

# from common.extensions import celery
from models.admin import admin
from common.utils import import_to_context


def create_app(name=__name__):
    app = Flask(name, template_folder='templates', static_folder='static')

    # load config file from settings.py first
    app.config.from_object('settings')

    # return json response
    app.response_class = JsonResponse

    # register a new converter
    app.url_map.converters.update(list=ListConverter)

    # register context processor
    register_context_processor(app, {
        'test': 'test<script>alert(1)</script>'
    })

    register_blueprints(app)

    register_commands(app)

    register_extensions(app)

    register_errorhandlers(app)

    register_shellcontext(app)

    return app


def register_extensions(app):
    """Register Flask extensions."""

    logger.init_app(app, 'flask.log')
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    admin.init_app(app)

    # KeyError: 'CELERY_BROKER_URL'
    # celery.init_app(app)

    bcrypt.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    webpack.init_app(app)

    return None


def register_blueprints(app, pkg='blueprints'):
    """register all blueprint modules in bp_pkg package
    """
    for name in find_modules(pkg):
        try:
            mod = import_string(name)
            if hasattr(mod, 'bp'):
                app.register_blueprint(mod.bp)
        except Exception as e:
            print '[{}]register blueprints: {}'.format(name, e)
    return None


def register_commands(app, pkg='commands'):
    """Register Click commands."""
    for name in find_modules(pkg):
        try:
            mod = import_string(name)
            if hasattr(mod, 'command'):
                app.cli.add_command(mod.command, name=name.split('.')[1])
        except Exception as e:
            print '[{}]register cmd: {}'.format(name, e)

    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.register_error_handler(errcode, render_error)
        # app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""

        extra_context = {
            'db': db
        }

        # import models to shell_context
        import_to_context('models', extra_context)
        # print 'Shell Context: %s' % extra_context
        return extra_context

    app.shell_context_processor(shell_context)


def register_teardowns(app, func):
    @app.teardown_appcontext
    def command(error):
        func()


def register_context_processor(app, extra_context):
    @app.context_processor
    def context():
        return extra_context
