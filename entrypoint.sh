#!/bin/bash

set -e

# En cas de virtuel
#source /env/bin/activate

python3 manage.py makemigrations
python3 manage.py migrate

if [ $1 == 'gunicorn' ]
then
 exec gunicorn compositions.wsgi:application -b 0.0.0.0:8000
else
 exec python3 manage.py runserver 0.0.0.0:8000
fi