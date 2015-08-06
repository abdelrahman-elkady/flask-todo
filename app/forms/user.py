from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators


class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=80)])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo(
        'confirm_password', message='Passwords are not matching')])

    confirm_password = PasswordField('Retype the password again')
    email = TextField('Email Address', [validators.Length(min=6, max=120)])
