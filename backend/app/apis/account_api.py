from app import db, jwt
from flask import jsonify
from app.models import Users
from flask_restx import Resource, fields, Namespace
from sqlalchemy.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, current_user

api = Namespace('account', 'Account Related Method')

@jwt.   user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return Users.query.filter_by(email=identity).one_or_none()

class PasswordProcess:
    def __init__(self, password):
        self.password = password
    def hashPassword(self):
        hashed_password = generate_password_hash(password=self.password)
        return hashed_password
    def checkPassword(self, check):
        check_password = check_password_hash(self.password, check)
        return check_password

account_register_input_data = api.model('register-input', {
    "username": fields.String('Username', required=True),
    "email": fields.String('Email', required=True),
    "password": fields.String('Password', required=True)
})

@api.route('/register')
class AccountRegister(Resource):
    @api.expect(account_register_input_data)
    def post(self):
        data = api.payload
        password = PasswordProcess(data['password'])
        data['password'] = password.hashPassword()
        user = Users(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(user)
        db.session.commit()
        return {"message": "Login-Succeed"}

account_login_input_data = api.model('login-input', {
    "email": fields.String(),
    "password": fields.String()
})

@api.route('/login')
class AccountLogin(Resource):
    @api.expect(account_login_input_data)
    def post(self):
        data = api.payload
        try:
            user = Users.query.filter_by(email=data['email']).first()
            if user == None:
                raise NoResultFound
            password = PasswordProcess(user.password)
            if password.checkPassword(data['password']):
                access_token = create_access_token(identity=data['email'])
                return {"access_token": access_token}
            else:
                return {"message": 'The password may be wrong'}
        except NoResultFound:
            return {"Error": "This user does not exist!!"}

@api.route('/info')
class AccountInfo(Resource):
    @jwt_required()
    def get(self):
        return {
            "username": current_user.id,
            "email": current_user.email
        }