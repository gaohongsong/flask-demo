uwsgi --gevent 100 --http 0.0.0.0:8000 --wsgi-file app.py --callable app --processes 4 --stats 0.0.0.0:5000
uwsgi --http 0.0.0.0:8000 --wsgi-file app.py --callable app --processes 9 --threads 4 --gevent --stats 0.0.0.0:5000
uwsgitop 0.0.0.0:5000
gunicorn -w 9 -k gevent -b 0.0.0.0:8000 app:app
