#!/bin/sh

set -e


python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn --bind 0.0.0.0:8000 --workers 4 --forwarded-allow-ips='frontend' backend.wsgi