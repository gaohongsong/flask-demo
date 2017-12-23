# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

name = 'error'
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


# @bp.errorhandler(404)
# def handle_404(error):
#     # response, status, headers
#     return render_template('404.html'), 404

@bp.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html', error=error), 404)
    resp.headers['X-Custom-Header'] = 'Something'
    return resp

