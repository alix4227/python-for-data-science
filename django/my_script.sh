#!/bin/bash
#lancer avec source pas .
python3 -m venv django_venv
 
django_venv/bin/pip install --upgrade pip
django_venv/bin/pip install -r requirement.txt
 
source django_venv/bin/activate
# sudo -u postgres psql -c "CREATE USER djangouser WITH PASSWORD 'secret';"
# sudo -u postgres psql -c "CREATE DATABASE formationdjango OWNER djangouser;"
