from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from flask_admin import Admin
from flask_basicauth import BasicAuth

# App configurations
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
Migrate(app, db)
CORS(app)
basic_auth = BasicAuth(app)
admin = Admin(app, template_mode="bootstrap4")
basic_auth = BasicAuth(app)

from app.admin import *

# Blueprint for apis
from .apis import blueprint as api
app.register_blueprint(api, url_prefix='/api')