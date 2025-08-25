FROM python:3.13-alpine AS builder

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.13-alpine AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    GRAPH_FILE="/data/graph.ttl"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY sparql_file/__init__.py ./sparql_file/__init__.py
COPY sparql_file/env.py ./sparql_file/env.py
COPY README.md ./README.md

CMD ["uvicorn", "sparql_file.env:app", "--host", "", "--port", "8080"]
