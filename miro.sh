#!/bin/bash

MIRO_SECRET_KEY=`head -c 40 /dev/random | base64`
SETTINGS_TEMPLATE="dev_settings.py.template"
SETTINGS_FILE="dev_settings.py"

if [ ! -f miro_pm/$SETTINGS_FILE ]; then
    echo "Create dev_settings.py"
    cp miro_pm/$SETTINGS_TEMPLATE miro_pm/$SETTINGS_FILE
    sed -i -e 's/INSERT_KEY_HERE/'$MIRO_SECRET_KEY'/g' miro_pm/$SETTINGS_FILE
fi

DJANGO_SETTINGS_MODULE='miro_pm.dev_settings'
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
python manage.py runserver
