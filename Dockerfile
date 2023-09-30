FROM python:3.9.18-slim-bullseye
LABEL authors="https://github.com/RaghwendraSingh"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /fastapi && \
    /fastapi/bin/pip install --no-cache-dir --upgrade pip && \
    apt-get update && \
    apt-get install -y gcc && \
    /fastapi/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ $DEV = "true"]; \
        then /fastapi/bin/pip install --no-cache-dir -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    rm -rf /var/lib/apt/lists/* && \
    adduser \
        --disabled-password \
        --no-create-home \
        fastapi-user

ENV PATH="/fastapi/bin:$PATH"

USER fastapi-user