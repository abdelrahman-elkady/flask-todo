from flask import Flask, render_template, url_for
from config import Config
from models import db
from views.user import user
from flask_wtf.csrf import CsrfProtect


csrf = CsrfProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    csrf.init_app(app)
    app.register_blueprint(user, url_prefix='/users')

    return app
