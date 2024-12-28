ARG APPROOT=/narayaneeyam
ARG STYLES_DIR=/narayaneeyam/ayuh_styles
ARG LOG_DIR="/var/log/ayuh"


FROM alpine:3.18 AS builder

ARG APPROOT

WORKDIR ${APPROOT}

RUN apk add --no-cache curl
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-arm64 \
    && mv tailwindcss-linux-arm64 tailwindcss \
    && chmod +x tailwindcss


FROM python:3.13.0-slim

ARG APPROOT
ARG STYLES_DIR
ARG LOG_DIR

COPY --from=builder ${APPROOT}/tailwindcss /usr/local/bin/tailwindcss
COPY .. ${APPROOT}/
WORKDIR ${APPROOT}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

ENV LOG_DIR=$LOG_DIR
ENV STYLES_DIR=$STYLES_DIR

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p "$LOG_DIR/gunicorn/"
RUN pip install --no-cache-dir gunicorn==21.2.0

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

CMD ["/bin/bash", "./entrypoint.sh"]



