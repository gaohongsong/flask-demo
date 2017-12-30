uwsgi --gevent 100 --http 0.0.0.0:8000 --wsgi-file app.py --callable app --processes 4 --stats 0.0.0.0:5000
uwsgi --http 0.0.0.0:8000 --wsgi-file app.py --callable app --processes 9 --threads 4 --gevent --stats 0.0.0.0:5000
uwsgitop 0.0.0.0:5000
gunicorn -w 9 -k gevent -b 0.0.0.0:8000 app:app

# https://blog.kgriffs.com/2012/12/18/uwsgi-vs-gunicorn-vs-node-benchmarks.html
uwsgi --http :8890 --file rse.py --gevent 2000 -l 1000 -p 1 -L
gunicorn \
  -b :8091 -w 1 -k gevent --worker-connections=2000 \
  --backlog=1000 -p gunicorn.pid --log-level=critical rse:ap

https://stackoverflow.com/questions/12340047/uwsgi-your-server-socket-listen-backlog-is-limited-to-100-connections
# error: Listen queue size is greater than the system max net.core.somaxconn (128)
sysctl -w net.core.somaxconn=4096
# 600 req/sec
uwsgi --gevent 2000 --http 0.0.0.0:8000 --wsgi-file app.py --callable app -p 1 --stats 0.0.0.0:5000 -L -l 1000
# 505 req/sec
gunicorn -w 1 -k gevent -b 0.0.0.0:8000 app:app --backlog=1000
