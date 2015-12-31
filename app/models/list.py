from app.database import db

from datetime import datetime


class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(80))
    items = db.relationship('Item')
    created_at = db.Column(db.DateTime)

    def __init__(self, title):
        self.title = title
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<List %r>' % self.title
