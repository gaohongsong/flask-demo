# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

name = 'api'
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


@bp.route('/demo/')
def demo():
    return {
        'result': True,
        'data': 123,
        'messge': 'success'
    }


@bp.route('/list/<list:names>/')
# @bp.route('/list/<list(separator="|"):names>/')
def list(names):
    return {
        'result': True,
        'data': names
    }
