from flask.ext.wtf import Form
from wtforms import TextField, validators


class NewListForm(Form):
    title = TextField('Title', [validators.Required(
        message='List title can\'t be empty')])
