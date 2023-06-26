FROM python:3.10-alpine

WORKDIR /app
COPY /app /app
COPY entrypoint.sh /bin/entrypoint

RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN pip install -r /app/requirements.txt && chmod +x /bin/entrypoint

CMD ["entrypoint"]