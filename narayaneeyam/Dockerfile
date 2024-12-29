ARG APPROOT=/narayaneeyam
ARG LOG_DIR="/var/log/ayuh"

FROM python:3.13.0-slim

ARG APPROOT
ARG LOG_DIR

WORKDIR ${APPROOT}
COPY .. ${APPROOT}/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

ENV LOG_DIR=$LOG_DIR

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p "$LOG_DIR/gunicorn/"
RUN pip install --no-cache-dir gunicorn==21.2.0

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

CMD ["/bin/bash", "./entrypoint.sh"]



