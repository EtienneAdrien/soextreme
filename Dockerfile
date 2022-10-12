# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app


RUN apk add --no-cache gcc musl-dev linux-headers libpq-dev python3-dev

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-interaction --no-ansi

EXPOSE 80
COPY ./app /app/app
COPY ./.env /app/.env

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/app"]
