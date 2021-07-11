FROM python:3.9-alpine

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

ENV PATH="${PATH}:/root/.local/bin"

RUN mkdir /app
WORKDIR /app/
COPY requirements/ /app/requirements
RUN pip install -r requirements/prod.txt
COPY entrypoint.sh /app/entrypoint.sh
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
