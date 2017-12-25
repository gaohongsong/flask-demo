# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

name = 'member'
bp = Blueprint(name, __name__, url_prefix='/%s' % name)


@bp.route('/')
@login_required
def members():
    """List members."""
    return render_template('member/members.html')
