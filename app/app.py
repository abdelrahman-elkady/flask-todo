from flask import Flask, render_template, url_for,redirect
from config import Config
from database import db
from views.user import user_blueprint,login_manager
from views.list import list_blueprint
from models.user import crypt
from config import csrf


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    csrf.init_app(app)
    crypt.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(list_blueprint,url_prefix='/lists')

    return app
