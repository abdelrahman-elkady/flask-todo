from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User,crypt
from app.forms.user import RegisterForm,LoginForm
from app.models import db

user = Blueprint(
    'user', __name__, template_folder='../templates/user')


from flask.ext.login import LoginManager,login_user,login_required,logout_user
login_manager = LoginManager()

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

@user.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Login and validate the user.
        if(user is not None and crypt.check_password_hash(user.password,form.password.data)):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('user.index'))
        else:
            flash('Username or password is not correct')
            return redirect(url_for('user.login'))

        # FIXME ... check next parameter later
        # next = flask.request.args.get('next')
        # if not next_is_valid(next):
        #     return flask.abort(400)


    return render_template('login.html', form=form)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
