# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""

from flask import (
    Flask, Blueprint, request, session, g,
    redirect, url_for, abort, render_template,
    flash, current_app, make_response
)

from flask_login import login_required, login_user, logout_user

from common.utils import flash_errors
from common.extensions import cache, login_manager
from forms.public import LoginForm
from forms.user import RegisterForm
from models.user import User

bp = Blueprint('root', __name__)


@cache.cached(timeout=50, key_prefix='all_comments')
def get_all_comments():
    print 'get_all_comments'
    comments = range(1000)
    return comments


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@bp.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('root/home.html', form=form)


@bp.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@bp.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('root.home'))
    else:
        flash_errors(form)
    return render_template('root/register.html', form=form)


@bp.route('/about/')
# @cache.cached(timeout=50)
def about():
    """About page."""
    current_app.logger.info('test only.')
    cached_comments = get_all_comments()
    form = LoginForm(request.form)
    return render_template('root/about.html', form=form)
