from celery import Celery
from celery.schedules import crontab
from datetime import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from mail import send_email
from config import Config

# Initiate Celery
app = Celery('tasks', broker=Config.BROKER_URI, bacend=Config.BACKEND_URI)
# Initiate SQLAlchemy engine
Base = declarative_base()
engine = create_engine(Config.DATABASE_URI)

from models import Subjects
from schema import *

'''
Use Marshmallow to make the data to jason format
Use event listener to watch whether the database changing
'''

# Create Session to get the data from every column
# Dump all columns of data


# Task to check whether the data time outdated or not
@app.task
def check_outdated():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        data = session.query(Subjects).filter_by(done=False).order_by(Subjects.reminding_date).order_by(Subjects.reminding_time).first()
        # data_json is a list of dict
        data_json = subject_schema.dump(data)
        time_now = dt.now()
        reminding_time = data_json['reminding_date'] + ' ' + data_json['reminding_time']
        # conver str time to datetime time
        reminding_time = dt.strptime(reminding_time, "%Y-%m-%d %H:%M")
        # if true then pop out the first one then go to the next
        if reminding_time <= time_now:
            send_email(subject_name=data_json['subject_name'], pages=data_json['pages'], 
                        detail=data_json['hw_detail'], reminding_time=reminding_time
            )
            data.done = True
            session.add(data)
            session.commit()
    except KeyError:
        pass

app.conf.beat_schedule = {
    "send-email-task": {
        "task": "tasks.check_outdated",
        "schedule": 10.0
    }
}
