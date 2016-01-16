from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort

from app.models import List, Item
from app.database import db
from app.forms.list import NewListForm
from app.config import csrf

from flask.ext.login import login_required, current_user

list_blueprint = Blueprint(
    'list', __name__, template_folder='../templates/list')

@list_blueprint.route('/<list_id>')
@login_required
def show(list_id):

    a_list = List.query.filter_by(id=list_id).first()

    items = Item.query.filter_by(list_id = list_id).all()
    return render_template('show.html',a_list = a_list, items= items)

@list_blueprint.route('/new',methods=['GET','POST'])
@login_required
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

@csrf.exempt
@list_blueprint.route('/delete/<list_id>',methods=['POST'])
@login_required
def delete(list_id):

    a_list = List.query.filter_by(id=list_id).first()

    if a_list:
        items=Item.query.filter_by(list_id=list_id).all()

        for item in items:
            db.session.delete(item)

        db.session.delete(a_list)
        db.session.commit()

    return '', 204 # no content
