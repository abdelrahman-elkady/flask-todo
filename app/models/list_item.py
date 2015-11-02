from app.database import db

from datetime import datetime

class ListItem(db.Model):
    __tablename__ = "list_items"
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self,content):
        self.content = content
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return 'Item %r' % content[:50]
