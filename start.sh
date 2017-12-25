#!/bin/sh

export FLASK_DEBUG=true
export FLASK_APP=app.py
flask run -h 0.0.0.0 -p 5000 --debugger --reload
