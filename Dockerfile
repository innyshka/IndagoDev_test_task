FROM python:3.11.4

LABEL maintainer = "inna8110302@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get -y install libpq-dev gcc
RUN pip install psycopg2

RUN pip install -r requirements.txt


RUN mkdir -p /vol/web/media

COPY . .


RUN adduser \
         --disabled-password \
         --no-create-home\
         django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
