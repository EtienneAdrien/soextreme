# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app


RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-interaction --no-ansi

EXPOSE 5000
COPY . .
CMD [ "uwsgi", "--ini", "app.ini" ]
