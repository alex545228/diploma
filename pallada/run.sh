#!/usr/bin/env bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate
python3 manage.py runserver 0:8000