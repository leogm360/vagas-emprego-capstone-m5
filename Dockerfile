FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --upgrade pip &&\
  pip install -r requirements.txt &&\
  apt-get update &&\
  apt-get install -y libpq-dev gcc bash curl openssh-server iproute2

ADD ./.profile.d /app/.profile.d

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /web_app

COPY . /web_app/
