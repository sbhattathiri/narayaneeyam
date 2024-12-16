FROM python:3.13.0-slim

EXPOSE 8000

ENV APPROOT /narayaneeyam
WORKDIR ${APPROOT}
COPY . ${APPROOT}/

# avoid .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# send stdout, stderr straightaway
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:${APPROOT}"

RUN pip install --no-cache-dir -r requirements.txt

# server
RUN mkdir -p /var/log/ayuh/gunicorn/
RUN pip install --no-cache-dir gunicorn==21.2.0
RUN chmod +x ./entrypoint.sh
CMD ["/bin/bash", "./entrypoint.sh"]



