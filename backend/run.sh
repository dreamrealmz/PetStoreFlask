#!/bin/sh

#python manager.py db migrate &&
python manager.py db upgrade &&

exec $@