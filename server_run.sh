#!/bin/bash -x

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

sudo ufw allow 8081

python manage.py runserver localhost:8081


