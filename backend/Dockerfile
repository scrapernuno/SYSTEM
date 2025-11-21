# backend/Dockerfile - usar Python 3.10 para compatibilidade com pandas 2.1.3
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# instalar dependências de sistema necessárias para surto de builds (pandas/numpy)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copiar requirements primeiro para cache de layers
COPY requirements.txt /app/requirements.txt

# pip moderno, wheel & setuptools antes de instalar dependências
RUN python -m pip install --upgrade pip setuptools wheel

# instalar requirements (irá preferir wheels binários, se existirem)
RUN pip install --no-cache-dir -r /app/requirements.txt

# copiar restante código
COPY . /app

# criar pastas que a app usa
RUN mkdir -p /app/uploads /app/output

EXPOSE 8000

# gunicorn já configurado no repo
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
