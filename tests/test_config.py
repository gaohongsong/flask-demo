# -*- coding: utf-8 -*-
"""Test configs."""
import os

from app_maker import create_app


def test_product_config():
    """Product config."""
    os.environ.setdefault('APP_ENV', 'product')
    app = create_app()
    assert app.config['ENV'] == 'product'
    assert app.config['DEBUG'] is False
    assert app.config['DEBUG_TB_ENABLED'] is False


def test_test_config():
    """Test config."""
    os.environ.setdefault('APP_ENV', 'test')
    app = create_app()
    assert app.config['ENV'] == 'test'
    assert app.config['DEBUG'] is True


def test_devlop_config():
    """Develop config."""
    # os.environ.setdefault('ENV', 'develop')
    app = create_app()
    assert app.config['ENV'] == 'develop'
    assert app.config['DEBUG'] is True
