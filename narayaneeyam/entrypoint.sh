#!/bin/sh
set -e

LOG_DIR=${LOG_DIR:-/var/log/app}
STARTUP_LOG_FILE="$LOG_DIR/startup.log"

GUNICORN_LOG_DIR="$LOG_DIR/gunicorn"
GUNICORN_ACCESS_LOG="$GUNICORN_LOG_DIR/access.log"
GUNICORN_ERROR_LOG="$GUNICORN_LOG_DIR/error.log"

echo "creating log directory..."
mkdir -p "$LOG_DIR"
mkdir -p "$GUNICORN_LOG_DIR"


echo "creating log file..."
touch "$STARTUP_LOG_FILE"
touch "$GUNICORN_ACCESS_LOG"
touch "$GUNICORN_ERROR_LOG"

printf "\n" | tee -a "$STARTUP_LOG_FILE"
date >> "$STARTUP_LOG_FILE"

echo "DJANGO_SETTINGS_MODULE" ${DJANGO_SETTINGS_MODULE} | tee -a "$STARTUP_LOG_FILE"
printf "\n" | tee -a "$STARTUP_LOG_FILE"

echo "make migrations..." | tee -a "$STARTUP_LOG_FILE"
python manage.py makemigrations --settings="${DJANGO_SETTINGS_MODULE}" >> "$STARTUP_LOG_FILE" 2>&1
printf "\n" | tee -a "$STARTUP_LOG_FILE"

echo "apply migrations..." | tee -a "$STARTUP_LOG_FILE"
python manage.py migrate --settings="${DJANGO_SETTINGS_MODULE}" >> "$STARTUP_LOG_FILE" 2>&1
printf "\n" | tee -a "$STARTUP_LOG_FILE"

echo "collect static..." | tee -a "$STARTUP_LOG_FILE"
python manage.py collectstatic --noinput --settings="${DJANGO_SETTINGS_MODULE}" >> "$STARTUP_LOG_FILE" 2>&1
printf "\n" | tee -a "$STARTUP_LOG_FILE"

echo "run..." | tee -a "$STARTUP_LOG_FILE"
gunicorn ayuh.wsgi \
 --timeout 120 \
 --workers $(($(nproc) * 2 + 1)) \
 --bind 0.0.0.0:8000 \
 --env DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE}" \
 --access-logfile "$GUNICORN_ACCESS_LOG" \
 --error-logfile "$GUNICORN_ERROR_LOG"

#tail -f /dev/null
#sleep infinity

