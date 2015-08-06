from flask.ext.script import Manager
from app import create_app
from app.models import db

app = create_app()
manager = Manager(app)


@manager.command
def runserver():
    app.run()


@manager.command
def drop_db():
    db.drop_all()


@manager.command
def init_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
