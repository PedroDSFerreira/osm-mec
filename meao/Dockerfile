# syntax=docker/dockerfile:1
FROM python:3.8
# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN sh osmclient-install.sh

CMD ["python", "app.py"]

