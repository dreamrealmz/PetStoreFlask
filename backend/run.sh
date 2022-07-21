#!/bin/sh

pip install -r requirements.txt

python manager.py db init &&
python manager.py db migrate &&
python manager.py db upgrade &&

exec $@