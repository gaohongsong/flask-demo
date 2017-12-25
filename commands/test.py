# -*- coding: utf-8 -*-
import os
import click
from flask import current_app
from flask.cli import with_appcontext


@click.command()
@with_appcontext
def command():
    """Run the tests."""
    TEST_PATH = os.path.join(current_app.root_path, 'tests')
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)
