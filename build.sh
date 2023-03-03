#!/bin/bash

python get-pip.py
python3.10 pip install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear