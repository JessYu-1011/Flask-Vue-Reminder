from . import db
from datetime import datetime

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # BackEnd for subject name but frontend use list to choose
    subject_name = db.Column(db.String(64), unique=False, nullable=False)
    # Subject owned by user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Format: x-y, x and y are two numbers
    pages = db.Column(db.String(30), nullable=False)
    hw_detail = db.Column(db.String(124), nullable=False)
    modify_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow())
    reminding_time = db.Column(db.String(30), nullable=False)
    reminding_date = db.Column(db.String(30), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)

class SubjectNames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(30), unique=True, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), unique=False, nullable=False)
    picture = db.Column(db.String(200), nullable=True)
    # One user has multiple subjects
    subjects = db.relationship('Subjects', backref='user', lazy='dynamic')