FROM python:3.12-slim-bullseye

WORKDIR /app/etl

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY etl.py .
