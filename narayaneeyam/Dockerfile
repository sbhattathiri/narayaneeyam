ARG APPROOT=/narayaneeyam
ARG LOG_DIR="/var/log/ayuh"

FROM python:3.13.1-slim-bookworm

ARG APPROOT
ARG LOG_DIR

WORKDIR ${APPROOT}
COPY .. ${APPROOT}/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

ENV LOG_DIR=$LOG_DIR

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn==21.2.0

RUN mkdir -p "$LOG_DIR/gunicorn/" && \
    addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

RUN chown -R appuser:appgroup ${APPROOT} && \
    chown -R appuser:appgroup "$LOG_DIR"

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

USER appuser

CMD ["/bin/bash", "./entrypoint.sh"]



