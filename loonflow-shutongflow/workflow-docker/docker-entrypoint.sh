#!/bin/bash
set -e

trap "kill -15 -1 && echo all proc killed" TERM KILL INT

if [ "$1" = "start" ]; then
    cd /opt/workflow/loonflow
    python3 manage.py makemigrations
    python3 manage.py migrate
    cd /opt/workflow/shutongFlow/apps
    python3 manage.py makemigrations
    python3 manage.py migrate
    #copy django css js files
    python3 manage.py collectstatic
    service redis-server start
    service nginx start
    service supervisor start
    sleep inf & wait
else
    exec "$@"
fi
