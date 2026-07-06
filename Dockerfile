FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /app/storage

EXPOSE 5000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "--timeout", "300", "app:app"]
