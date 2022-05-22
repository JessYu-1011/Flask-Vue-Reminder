import json

with open('./config/tasks-config.json') as config_file:
    config = json.load(config_file)

class Config:
    # The database URI
    DATABASE_URI = config.get('DATABASE_URI')
    # Celery setting
    BROKER_URI = config.get('BROKER_URI')
    BACKEND_URI = config.get('BACKENd_URI')
    # MAIL config
    MAIL_ACCOUNT = config.get('MAIL_ACCOUNT')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    TO_ADDR = config.get('TO_ADDR')