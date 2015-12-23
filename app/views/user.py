from flask import Blueprint, render_template, redirect, url_for, request, flash, abort

from app.models import User, List
from app.models.user import crypt
from app.forms.user import RegisterForm, LoginForm
from app.database import db

from flask.ext.login import LoginManager, login_user, login_required, logout_user, current_user

import re

user_blueprint = Blueprint(
    'user', __name__, template_folder='../templates/user')

login_manager = LoginManager()
login_manager.login_view = 'user.login'


@user_blueprint.route('/')
@login_required
def index():
    user = current_user
    lists = user.lists
    return render_template('index.html', lists=lists)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data, form.email.data)

        # FIXME handle unique constraint in more efficient way !
        if len(User.query.filter_by(username=user.username).all()) > 0:
            flash('Username is already taken')
            return render_template('register.html', form=form)

        if len(User.query.filter_by(email=user.email).all()) > 0:
            flash('Email is already taken')
            return render_template('register.html', form=form)

        db.session.add(user)
        db.session.commit()
        flash('Successfully registered')
        return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Login and validate the user.
        if(user is not None and crypt.check_password_hash(user.password, form.password.data)):
            login_user(user)
            flash('Logged in successfully')
            next = request.args.get('next')
            if not validate_next(next):
                return abort(400)
            else:
                return redirect(next or url_for('user.index'))
        else:
            flash('Username or password is not correct')
            return redirect(url_for('user.login'))

    return render_template('login.html', form=form)


@user_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('user.index'))


@login_manager.user_loader
def load_user(user_id):
    """ user loader for flask-login """
    return User.query.get(user_id)


def validate_next(url):
    """ validates next parameter """
    if url is None:
        return True
    re1 = '^\/[a-z0-9/.&=?]*'

    rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
    return rg.search(url) is not None
