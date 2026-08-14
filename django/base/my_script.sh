#!/bin/bash
#lancer avec source pas .
python3 -m venv django_venv
 
django_venv/bin/pip install --upgrade pip
django_venv/bin/pip install -r requirements.txt
django_venv/bin/pip install django-browser-reload
source django_venv/bin/activate
