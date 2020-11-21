import gevent.monkey
gevent.monkey.patch_all()

import os
import multiprocessing


DEBUG = os.environ.get('DEBUG', False)

bind = '0.0.0.0:5000'
workers = int(os.environ.get('DJANGO_WORKERS', 1 if DEBUG else multiprocessing.cpu_count() * 2))
threads = multiprocessing.cpu_count()
worker_class = 'gevent'
accesslog = '-'
errorlog = '-'
loglevel = 'debug' if DEBUG else 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'
proc_name = 'gunicorn-any-tools'
timeout = 300
