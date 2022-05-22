from .. import app, db
from flask import request, abort, redirect, render_template, url_for
from flask_restx import Resource, Namespace, fields
from ..models import User

api = Namespace('users', 'User Related Method')
# Read the Client ID from config
CLIENT_ID = app.config.get('CLIENT_ID')

post_data = {
    "email": fields.String(required=True, description="User's email"),
    "name": fields.String(required=True, description="User's name"),
    "picture": fields.String(required=True, description="User's picture"),
}

@api.route('/login/google')
class GoogleLogin(Resource):
    def post(self):
        try:
            email = request.json.get('email')
            picture = request.json.get('picture')
            name = request.json.get('name')
            user = User(
                email=email,
                name=name,
                picture=picture
            )
            db.session.add(user)
            db.session.commit()
            
            return {
                'message': 'success'
            }, 200
        except ValueError:
            return {"message": "The value is invalid"}