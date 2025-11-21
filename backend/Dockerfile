FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies for compiling packages like pandas if wheels not available
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    python3-dev \
    pkg-config \
    ninja-build \
    libopenblas-dev \
    liblapack-dev \
    libblas-dev \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

# upgrade pip/setuptools/wheel and install Cython to assist builds
RUN python -m pip install --upgrade pip setuptools wheel cython

# Install Python dependencies (may compile if wheels are not available)
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN mkdir -p /app/uploads /app/output

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
