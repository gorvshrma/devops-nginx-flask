# Stage 1: Build dependencies
FROM cgr.dev/chainguard/python:latest-dev AS builder

WORKDIR /app

# Copy requirements before installing dependencies
COPY requirements.txt .

# Create virtual environment and install dependencies
RUN python -m venv /app/venv \
    && /app/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && rm -rf /app/venv/lib/python*/site-packages/pip \
              /app/venv/lib/python*/site-packages/pip-*.dist-info

# Stage 2: Minimal production runtime
FROM cgr.dev/chainguard/python:latest

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/venv/bin:$PATH"

WORKDIR /app

COPY --from=builder /app/venv /app/venv
COPY app.py /app/app.py

USER 65532:65532

EXPOSE 5000

ENTRYPOINT ["/app/venv/bin/python"]

CMD ["-m", "gunicorn", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "2", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "app:app"]