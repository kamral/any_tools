#!/bin/sh

set -ex

export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-any_tools.settings.dev}

case $1 in
    serve)
        cmd="/usr/bin/gunicorn --config gunicorn_conf.py any_tools.wsgi:application"
    ;;
    migrate)
        cmd="python3 manage.py migrate"
    ;;
    *)
        cmd="$@"
    ;;
esac

exec $cmd
