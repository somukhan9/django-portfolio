#!/bin/bash

echo "Building the project...."
pip install -r requirements.txt
echo "Collecting staticfiles"
python3.10 manage.py collectstatic --noinput --clear