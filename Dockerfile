FROM python:3.9.6

RUN apt-get install libpq-dev

RUN mkdir /social_networking_app

WORKDIR /social_networking_app

ADD . /social_networking_app/

RUN pip install -r requirements.txt
