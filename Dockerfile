FROM python:3.6-alpine

LABEL maintainer="kirillsulim@gmail.com"

RUN mkdir -p /app/src
COPY ./setup.py /app
COPY ./README.md /app
COPY ./src /app/src

WORKDIR /app

RUN python setup.py install

ENTRYPOINT [ "desman" ] 
