# -*- coding: utf-8 -*-
"""
# app.run(host='0.0.0.0', port=5000, debug=app.debug)
flask run -h 0.0.0.0 -p 5000 --debugger --reload
"""
from app_maker import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
