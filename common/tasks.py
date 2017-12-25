# -*- coding: utf-8 -*-
from app import celery, app


@celery.task()
def add_together(a, b):
    app.logger.info('hello world')
    return a + b
