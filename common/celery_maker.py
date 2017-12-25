# -*- coding: utf-8 -*-
"""
make celery for flask
http://docs.jinkan.org/docs/flask/patterns/celery.html
http://flask.pocoo.org/docs/0.12/patterns/celery/
"""
from celery import Celery


def make_celery(app):
    """
        The function creates a new Celery object, configures it with the broker
        from the application config, updates the rest of the Celery config from
        the Flask config and then creates a subclass of the task that wraps the
        task execution in an application context.
    """
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BORKER_URL']
    )
    celery.conf.update(app.config)

    TaskBase = celery.Task

    # creates a subclass of the task
    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            # wraps the task execution in an application context
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    # patch task
    celery.Task = ContextTask

    return celery
