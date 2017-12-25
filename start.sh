#!/bin/sh

help() {
echo """
=======================================================
$0 [debug]    --     debug[on] + auto reload[on]
$0            --     debug[off]
=======================================================
"""
}

help

export FLASK_APP=app.py
if [[ $1 == 'debug' ]]; then
    FLASK_DEBUG=true && flask run -h 0.0.0.0 -p 5000 --debugger --reload &
else
    FLASK_DEBUG=false flask run -h 0.0.0.0 -p 5000 &
fi

echo 'start celery worker...'
echo 'celery -A app.celery worker -l info -c 2'
celery -A app.celery worker -l info -c 2 &

