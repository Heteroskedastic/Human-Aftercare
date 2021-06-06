#!/bin/bash

BRANCH=master

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $PARAM in
       --skip-collectstatic)
            SKIP_COLLECTSTATIC=true;
            ;;
       --branch)
            BRANCH=$VALUE
            ;;
   esac
    shift
done

NAME="human_aftercare"
GITURL=https://github.com/Heteroskedastic/Human-Aftercare.git
ROOTDIR=/opt/webapps
PROJECTDIR=${ROOTDIR}/${NAME}
DJANGODIR=${PROJECTDIR}/${NAME}
ENVDIR=${PROJECTDIR}/env
DJANGO_SETTINGS_MODULE=human_aftercare.settings.main

echo "+++ Deploying $NAME: BRANCH=$BRANCH PROJECTDIR=$PROJECTDIR ..."

mkdir -p ${PROJECTDIR}
mkdir -p ${PROJECTDIR}/run
mkdir -p ${PROJECTDIR}/logs
mkdir -p ${PROJECTDIR}/etc
mkdir -p ${PROJECTDIR}/tmp

if [ -d "$DJANGODIR" ]; then
    cd ${DJANGODIR}
    git reset --hard HEAD
    git pull origin
    git checkout ${BRANCH}
    git pull
else
    git clone ${GITURL} -b ${BRANCH} ${DJANGODIR}
fi
sudo supervisorctl stop ${NAME}
sleep 1
if [ ! -d "$ENVDIR" ]; then
    virtualenv -p python3 ${ENVDIR}
fi
source ${ENVDIR}/bin/activate
cp ${DJANGODIR}/utils/gunicorn_start.sh ${ENVDIR}/bin/
chmod +x ${ENVDIR}/bin/gunicorn_start.sh
cp ${DJANGODIR}/utils/daphne_start.sh ${ENVDIR}/bin/
chmod +x ${ENVDIR}/bin/daphne_start.sh
cd ${DJANGODIR}
pip install -r requirements.txt
pip install django-gunicorn
pip install daphne
cd ${DJANGODIR}/human_aftercare
python manage.py migrate --settings=${DJANGO_SETTINGS_MODULE} --noinput
if [ -z "$SKIP_COLLECTSTATIC" ]; then
    python manage.py collectstatic --settings=${DJANGO_SETTINGS_MODULE} --noinput
fi
sudo supervisorctl start ${NAME}
sudo service supervisor restart
sudo service nginx restart

echo
echo "Finished!"
