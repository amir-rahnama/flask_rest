FROM python:3
MAINTAINER Amir Rahnama "amirrahnama@gmail.com"

COPY . /app
WORKDIR /app

RUN pip install -r requirement.txt
RUN pip install --editable .

ENV FLASK_APP mini/app.py
RUN flask initdb

EXPOSE 5000

CMD python -m flask run --host=0.0.0.0

