from flask_restx import Api
from flask import Blueprint
from .subjects import api as ns1
from .users import api as ns2

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title = 'API',
    version='1.0',
    doc='/doc'
)

api.add_namespace(ns1, path='/subjects')
api.add_namespace(ns2, path='/users')