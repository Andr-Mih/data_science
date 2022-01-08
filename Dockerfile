FROM python:3-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /web_app
ADD . /web_app
COPY requirements.txt /web_app/
RUN pip install --upgrade pip && pip install -r requirements.txt