from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort

from app.models import List
from app.database import db
from app.forms.list import NewListForm

from flask.ext.login import login_required, current_user

list_blueprint = Blueprint(
    'list', __name__, template_folder='../templates/list')


@list_blueprint.route('/new',methods=['GET','POST'])
def new():
    form = NewListForm(request.form)

    if request.method == 'POST' and form.validate():
        new_list = List(form.title.data)
        current_user.lists.append(new_list)

        db.session.add(new_list)
        db.session.add(current_user)
        db.session.commit()

        flash('New list created successfully')

        return redirect(url_for('user.index'))

    return render_template('new.html', form=form)
