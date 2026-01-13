FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


# ---------- Dev ----------
FROM base AS dev
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# ---------- Prod ----------
FROM base AS prod
CMD ["gunicorn", "tu_proyecto.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "60"]