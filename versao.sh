#!/bin/bash

cd /home/ubuntu/gestao_rh
sudo git pull origin main
sudo pip install -r requirements.txt
sudo python3 manage.py migrate
sudo systemctl restart uwsgi_gestao_rh