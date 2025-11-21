# backend/Dockerfile - use Python 3.10 and install required build deps
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install build deps and BLAS/LAPACK libraries available on Debian trixie
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    pkg-config \
    libopenblas-dev \
    liblapack-dev \
    libblas-dev \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy requirements first for layer caching
COPY requirements.txt /app/requirements.txt

# upgrade pip/wheel/setuptools to favour wheels
RUN python -m pip install --upgrade pip setuptools wheel

# install python requirements
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy app code
COPY . /app

# create expected directories
RUN mkdir -p /app/uploads /app/output

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
