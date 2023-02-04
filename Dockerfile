FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get install libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .