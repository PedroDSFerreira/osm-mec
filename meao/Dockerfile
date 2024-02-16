# syntax=docker/dockerfile:1
FROM python:3.8
# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY osmclient-install.sh osmclient-install.sh
RUN sh osmclient-install.sh

CMD ["python", "app.py"]
