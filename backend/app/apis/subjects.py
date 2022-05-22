from app import db
from flask_restx import Resource, fields, Namespace
from app.models import Subjects, SubjectNames
from app.schema import *
from datetime import datetime
from flask import request
from sqlalchemy.exc import IntegrityError


api = Namespace('subjects', 'Subjects Related Method')

# The format to output data
subject_output_data = {
    'id': fields.Integer,
    'subject_name': fields.String('name'),
    'hw_detail': fields.String('description'),
    'reminding_time': fields.String('reminding_time'),
    'reminding_date': fields.String('reminding_date'),
    'modify_time': fields.DateTime(dt_format='iso8601'),
    'pages': fields.String('pages')
}

# The format to input data
subject_input_data = {
    'name': fields.String('name'),
    'detail': fields.String('description'),
    'pages': fields.String('pages'),
    'reminding_time': fields.String('time'),
    'reminding_date': fields.String('reminding_date'),
}

subject_names_output_data = {
    "id": fields.String('subject_names_id'),
    "subject_name": fields.String('subject_names_name')
}

subject_names_input_data = {
    "subject_name": fields.String('subject_names_name')
}

# For frontedn to create a list
@api.route('/info')
class SubjectsInfo(Resource):
    @api.marshal_with(subject_output_data)
    def get(self):
        subjects = Subjects.query.filter_by(done=False).order_by(Subjects.id).all()
        subject_output = subjects_schema.dump(subjects)
        return subject_output

# To modify each id detail
@api.route('/modify/<int:subject_id>')
class SubjectModify(Resource):
    @api.marshal_with(subject_output_data)
    def get(self, subject_id):
        subject = Subjects.query.filter_by(id=subject_id, done=False).first()
        subject_output = subject_schema.dump(subject)
        return subject_output

    @api.expect(subject_input_data)
    @api.marshal_with(subject_output_data)
    def put(self, subject_id):
        subject = Subjects.query.filter_by(id=subject_id).first()
        body = api.payload
        data = body['data']
        subject.subject_name = data['name']
        subject.hw_detail = data['detail']
        subject.reminding_time = data['reminding_time']
        subject.reminding_date = data['reminding_date']
        subject.pages = data['pages']
        db.session.add(subject)
        db.session.commit()
    
    def delete(self, subject_id):
        subject = Subjects.query.filter_by(id=subject_id).first()
        db.session.delete(subject)
        db.session.commit()

# To create a new data
@api.route('/create')
class SubjectCreate(Resource):
    
    @api.expect(subject_input_data)
    @api.marshal_with(subject_output_data)
    def post(self):
        # frontend will send the body to backend
        '''
        It will be like
        headers: {'Content-Type': 'application/json'},
        data: {'name': 'xxx', 'pages': 'xxx', 'detail': 'xxxx', 'reminding_time': 'xxx'}
        '''
        body = api.payload
        data = body['data']
        # Time must be a String
        # It just have " %Y-%m-%d %H:%M"
        subject = Subjects(subject_name=data['name'], 
                            hw_detail=data['detail'], 
                            reminding_time=data['reminding_time'],
                            reminding_date=data['reminding_date'],
                            pages=data['pages'])
        db.session.add(subject)
        db.session.commit()

@api.route('/subject_names_list')
class SubjectNamesListInfo(Resource):
    def get(self):
        data = SubjectNames.query.order_by(SubjectNames.id).all()
        subject_name_output = subject_names_schema.dump(data)
        return subject_name_output

    @api.expect(subject_names_input_data)
    @api.marshal_with(subject_names_output_data)
    def post(self):
        body = api.payload
        data = body['data']
        subject_name = SubjectNames(subject_name=data['subject_name'])
        # The subject_name column is unique, so if it has been set already
        # It will casuse the exception
        try:
            db.session.add(subject_name)
            db.session.commit()
        except IntegrityError:
            return "The value has been set"

    @api.expect(subject_names_input_data)
    def delete(self):
        data = api.payload
        
        subject_name = SubjectNames.query.filter_by(subject_name=data['subject_name']).first()
        db.session.delete(subject_name)
        db.session.commit()

@api.route('/subject_names_list/<int:id>')
class SubjectNamesListModification(Resource):
    @api.expect(subject_names_input_data)
    @api.marshal_with(subject_names_output_data)
    def put(self, id):
        subject_name = SubjectNames.query.filter_by(id=id).first()
        body = api.payload
        data = body['data']
        subject_name.subject_name = data['subject_name']
        db.session.add(subject_name)
        db.session.commit()