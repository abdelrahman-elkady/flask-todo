from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///todo_db'
    SECRET_KEY = 'aV3rySEcr3tK3yJustForDevelopment'
