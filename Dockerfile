FROM python

ENV PYTHONUMBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install django six django

EXPOSE 80 8080 8000
