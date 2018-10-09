FROM ubuntu:latest
FROM python:latest
RUN apt-get update -y
EXPOSE 5000
COPY . /app
RUN mkdir -p /data/db
WORKDIR /app
ENV PATH=/app:$PATH
RUN pip3 install -r requirements.txt
ENV FLASK_APP app.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
