FROM python:3.9.1-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
