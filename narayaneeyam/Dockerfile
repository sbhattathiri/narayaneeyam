ARG APPROOT=/narayaneeyam
ARG LOG_DIR="/var/log/ayuh"

FROM python:3.13.1-slim-bookworm

ARG APPROOT
ARG LOG_DIR

# weasyprint pdf
ENV XDG_CACHE_HOME=/tmp/.cache

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    libgdk-pixbuf2.0-0 \
    libxml2 \
    libxslt1.1 \
    libjpeg-dev \
    zlib1g-dev \
    shared-mime-info \
    curl \
    fonts-dejavu \
    fonts-dejavu-core \
    fonts-noto-core \
    fonts-noto-unhinted \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    fonts-noto-extra \
    && mkdir -p /tmp/.cache/fontconfig \
    && chmod -R 777 /tmp/.cache \
    && fc-cache -f -v \
    && rm -rf /var/lib/apt/lists/*


WORKDIR ${APPROOT}
COPY .. ${APPROOT}/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

ENV LOG_DIR=$LOG_DIR

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn==21.2.0

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

RUN mkdir -p "$LOG_DIR"

RUN chown -R appuser:appgroup ${APPROOT} && \
    chown -R appuser:appgroup "$LOG_DIR"

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

USER appuser

CMD ["/bin/bash", "./entrypoint.sh"]



