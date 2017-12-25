# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

name = 'user'
bp = Blueprint('user', __name__, url_prefix='/users')


@bp.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')
