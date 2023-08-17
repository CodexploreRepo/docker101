FROM python:3.11-slim

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip \    
    && pip install --no-cache-dir -r requirements.txt

COPY db_connector.py .