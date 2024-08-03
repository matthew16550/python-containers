# checkov:skip=CKV_DOCKER_2:HEALTHCHECK not relevant
# checkov:skip=CKV_DOCKER_3:USER not relevant

FROM docker.io/library/python:3.12.4-slim-bookworm

WORKDIR /app

COPY requirements.txt .

# hadolint ignore=DL3042
RUN --mount=type=cache,id=pip,target=/root/.cache \
    pip install --root-user-action=ignore -r requirements.txt

ENTRYPOINT ["/usr/local/bin/vdirsyncer"]
