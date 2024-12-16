#!bin/sh

LOG_FILE="/var/log/ayuh/startup.log"

echo "creating log directory..."
mkdir -p "$(dirname "$LOG_FILE")"

echo "creating log file..."
touch "$LOG_FILE"

printf "\n" | tee -a "$LOG_FILE"
date >> "$LOG_FILE"

echo "DJANGO_SETTINGS_MODULE" ${DJANGO_SETTINGS_MODULE} | tee -a "$LOG_FILE"
printf "\n" | tee -a "$LOG_FILE"

echo "make migrations..." | tee -a "$LOG_FILE"
python manage.py makemigrations --settings="${DJANGO_SETTINGS_MODULE}" >> "$LOG_FILE" 2>&1
printf "\n" | tee -a "$LOG_FILE"

echo "apply migrations..." | tee -a "$LOG_FILE"
python manage.py migrate --settings="${DJANGO_SETTINGS_MODULE}" >> "$LOG_FILE" 2>&1
printf "\n" | tee -a "$LOG_FILE"

echo "collect static..." | tee -a "$LOG_FILE"
python manage.py collectstatic --noinput --settings="${DJANGO_SETTINGS_MODULE}" >> "$LOG_FILE" 2>&1
printf "\n" | tee -a "$LOG_FILE"

echo "run..." | tee -a "$LOG_FILE"
gunicorn ayuh.wsgi \
 --timeout 1200 \
 --workers $(($(nproc) * 2 + 1)) \
 --bind 0.0.0.0:8000 \
 --env DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE}" \
 --env settings="${DJANGO_SETTINGS_MODULE}" \
 --access-logfile /var/log/almamater/gunicorn/access.log \
 --error-logfile /var/log/almamater/gunicorn/error.log

tail -f /dev/null

