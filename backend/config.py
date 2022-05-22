import json

with open('./config/reminder-config.json') as config_file:
    config = json.load(config_file)

class Config:
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config.get('SECRET_KEY')
    CLIENT_ID = config.get('CLIENT_ID')
    # BASIC_AUTH_USERNAME = config.get('BASIC_AUTH_USERNAME')
    # BASIC_AUTH_PASSWORD = config.get('BASIC_AUTH_PASSWORD')
    # BASIC_AUTH_FORCE = True
