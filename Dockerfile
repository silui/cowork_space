FROM python

ENV PYTHONUMBUFFERED 1

RUN mkdir /code

WORKDIR /code

EXPOSE 80 8080 8000

RUN pip install django six django psycopg2

