FROM foo

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,id=pip,target=/root/.cache \
    pip install --root-user-action=ignore -r requirements.txt

CMD "/usr/local/bin/vdirsyncer"
