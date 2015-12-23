from flask.ext.login import LoginManager, login_required
from app.database import db

from datetime import datetime
from flask.ext.bcrypt import Bcrypt

crypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(250))
    email = db.Column(db.String(120), unique=True)
    lists = db.relationship("List")
    registered_on = db.Column(db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.lists = []
        self.registered_on = datetime.utcnow()

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password(self, password):
        self.password = crypt.generate_password_hash(password)
