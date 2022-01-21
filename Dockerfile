FROM python:3.10-alpine

ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ARG PYTHON_VERSION=3.10

WORKDIR /app

RUN apk add --no-cache \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
    source $HOME/.cargo/env && \
    pip install --no-cache-dir poetry && \
    apk del \
        curl \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev

COPY . .

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-dev

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["uvicorn", "api.infra.entrypoint:app", "--host", "0.0.0.0", "--port", "80"]
