#!/bin/bash

USER=pro                                           # the user to run as
NAME="corpecumig"                                   # Name of the application
DJANGODIR=/home/$USER/webapps/$NAME/corporacion           # Django project directory
SOCKFILE=/home/$USER/webapps/$NAME/gunicorn.sock  # we will communicte using this unix socket
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn

# GROUP=webapps                                     # the group to run as
# DJANGO_SETTINGS_MODULE=hello.settings             # which settings file should Django use
# DJANGO_WSGI_MODULE=hello.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/$USER/.virtualenvs/$NAME/bin/activate
export DJANGO_SETTINGS_MODULE=corporacion.settings.production
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/$USER/.virtualenvs/$NAME/bin/gunicorn corporacion.wsgi:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --bind=unix:$SOCKFILE
