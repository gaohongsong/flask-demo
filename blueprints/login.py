# -*- coding: utf-8 -*-

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

name = 'auth'
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                        request.form['password'] != 'admin':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    current_app.logger.error('please login first.')
    return render_template('login.html', error=error)


@bp.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
