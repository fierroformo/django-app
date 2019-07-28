FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /src

WORKDIR /src

ADD ./src /src

RUN pip install -r requirements/local.txt
