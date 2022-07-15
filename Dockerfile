FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /web_app

COPY . /web_app/

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install psycopg2