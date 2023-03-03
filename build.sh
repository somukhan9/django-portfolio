#!/bin/bash

echo "Building the project...."
python -m pip install -r requirements.txt
echo "Collecting staticfiles"
python manage.py collectstatic --noinput --clear