from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User
from app.forms.user import RegisterForm
from app.models import db

user = Blueprint(
    'user', __name__, template_folder='../templates/user')


@user.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data ,form.email.data)
        db.session.add(user)
        db.session.commit()  # FIXME wanna commit ?
        flash('Successfully registered')
        return redirect(url_for('user.index'))

    return render_template('register.html', form=form)
