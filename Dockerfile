FROM node:22.12.0-alpine3.20 AS tailwind-builder

ARG FRONTEND_APPROOT=/narayaneeyam-frontend
ARG BACKEND_APPROOT=/narayaneeyam-backend

WORKDIR ${FRONTEND_APPROOT}
COPY frontend/ ${FRONTEND_APPROOT}/

RUN cd css && \
    npm install && \
    npm run build:css


FROM python:3.13.0-slim

ARG FRONTEND_APPROOT=/narayaneeyam-frontend
ARG BACKEND_APPROOT=/narayaneeyam-backend

WORKDIR ${BACKEND_APPROOT}
COPY backend/ ${BACKEND_APPROOT}/

# tailwind css
COPY --from=tailwind-builder /${FRONTEND_APPROOT}/css/dist/styles.css .${BACKEND_APPROOT}/static/css/styles.css

# avoid .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# send stdout, stderr straightaway
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${BACKEND_APPROOT}"

RUN pip install --no-cache-dir -r requirements.txt

# server
RUN mkdir -p /var/log/ayuh/gunicorn/ && \
    pip install --no-cache-dir gunicorn==21.2.0

EXPOSE 8000

RUN chmod +x ./entrypoint.sh

CMD ["/bin/bash", "./entrypoint.sh"]



