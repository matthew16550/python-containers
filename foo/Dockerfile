# checkov:skip=CKV_DOCKER_2:HEALTHCHECK not relevant

FROM docker.io/library/python:3.12.2-slim-bookworm

WORKDIR /app

COPY requirements.txt .

# hadolint ignore=DL3042
RUN --mount=type=cache,id=pip,target=/root/.cache \
    pip install --root-user-action=ignore -r requirements.txt

CMD ["/usr/local/bin/vdirsyncer"]
