#!bin/sh

LOG_FILE="$LOG_DIR/startup.log"

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

echo "copy css..." | tee -a "$LOG_FILE"
tailwindcss -i "$STYLES_DIR/styles.css" -o "$STYLES_DIR/dist/output.css"
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
 --access-logfile "$LOG_DIR/gunicorn/access.log" \
 --error-logfile "$LOG_DIR/gunicorn/error.log"

#tail -f /dev/null
#sleep infinity

