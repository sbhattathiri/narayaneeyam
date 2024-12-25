ARG APPROOT=/narayaneeyam
ARG FRONTEND_DIR=/narayaneeyam/ayuh_frontend
ARG LOG_DIR="/var/log/ayuh"

FROM python:3.13.0-slim

ARG APPROOT
ARG FRONTEND_DIR
ARG LOG_DIR

COPY . ${APPROOT}/
WORKDIR ${APPROOT}

# avoid .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# send stdout, stderr straightaway
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

# setting ENV for use in entrypoint.sh
ENV LOG_DIR=$LOG_DIR
ENV FRONTEND_DIR=$FRONTEND_DIR

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p "$LOG_DIR/gunicorn/"
RUN pip install --no-cache-dir gunicorn==21.2.0

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

CMD ["/bin/bash", "./entrypoint.sh"]



