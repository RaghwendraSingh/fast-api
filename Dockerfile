FROM python:3.9.18-slim-bullseye
LABEL authors="https://github.com/RaghwendraSingh"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tm/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /fastapi && \
    /fastapi/bin/pip install --upgrade pip && \
    apt-get update && \
    apt-get install gcc && \
    /fastapi/bin/pip intall -r /tmp/requirements.txt && \
    if [ ${DEV} = "true"]; \
        then /fastapi/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    rm -rm /var/lib/apt/lists/* && \
    adduser \
        --disabled-password \
        --no-create-home \
        fastapi-user

ENV PATH="/fastapi/bin:$PATH"

USER fastapi-user