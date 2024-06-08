FROM docker.io/library/python:3.12.3-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install --root-user-action=ignore -r requirements.txt
