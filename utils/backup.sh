#!/bin/bash

NAME="human_aftercare"
ROOTDIR=/opt/webapps
PROJECTDIR=${ROOTDIR}/${NAME}
DJANGODIR=${PROJECTDIR}/${NAME}
ENVDIR=${PROJECTDIR}/env
DJANGO_SETTINGS_MODULE=human_aftercare.settings.main
BACKUP_DIR=${PROJECTDIR}/backup/`date +"%Y-%m-%d-%H-%M-%S"`.$RANDOM

echo "+++ Backing up $NAME to $BACKUP_DIR ..."
source ${ENVDIR}/bin/activate
cd ${DJANGODIR}/human_aftercare

mkdir -p ${BACKUP_DIR}

python manage.py dbbackup -O ${BACKUP_DIR}/db.sql --settings=${DJANGO_SETTINGS_MODULE} --noinput
# this will get the private media
python manage.py mediabackup -z -O ${BACKUP_DIR}/media.zip --settings=${DJANGO_SETTINGS_MODULE} --noinput
# this will get the public media
env DJANGO_EXTERNAL_CONFIG_JSON='{"AWS_STORAGE_BUCKET_NAME": "wrh-photos-assets-public-dev"}' python manage.py mediabackup -z -O ${BACKUP_DIR}/media2.zip --settings=${DJANGO_SETTINGS_MODULE} --noinput

echo
echo "Finished Backup!"
