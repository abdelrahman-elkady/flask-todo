from flask.ext.script import Manager
from app import create_app
from app.models import db
from flask import url_for

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

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:40s} {:30s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


if __name__ == '__main__':
    manager.run()
