FROM python:3.9.9

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD uwsgi --ini app.ini