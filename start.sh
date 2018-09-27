#!/bin/bash
source .env/bin/activate
nohup uwsgi --http :5490 --threads 10 --module bot_app:app 1>>server.log 2>&1 &
