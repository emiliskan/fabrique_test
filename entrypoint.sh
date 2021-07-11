#!/bin/sh
gunicorn config.wsgi:application -t 300 -w 4 -b 0.0.0.0:8000 --reload
exec "$@"
