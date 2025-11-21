FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN mkdir -p /app/uploads /app/output

EXPOSE 8000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
