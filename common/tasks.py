# -*- coding: utf-8 -*-
from app import celery, app


@celery.task()
def add_together(a, b):
    app.logger.info('hello world')
    return a + b

# from common.extensions import celery
# from flask import current_app
#
#
# @celery.task()
# def add_together(a, b):
#     current_app.logger.info('hello world')
#     return a + b
