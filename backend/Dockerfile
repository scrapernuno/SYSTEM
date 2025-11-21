FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
RUN mkdir -p /app/uploads /app/output

EXPOSE 8000

# Use PORT env var if set by the platform, default to 8000.
ENTRYPOINT ["sh", "-c", "exec gunicorn app:app -b 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120"]
