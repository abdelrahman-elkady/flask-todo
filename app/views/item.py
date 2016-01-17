from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort

from app.config import csrf

from app.models import Item,List
from app.database import db

from flask.ext.login import login_required, current_user

item_blueprint = Blueprint(
    'item', __name__, template_folder='../templates/item')

@item_blueprint.route('/new', methods=['POST'])
@csrf.exempt
@login_required
def new():
    data = request.get_json()

    a_list = List.query.filter_by(id=int(data['list_id'])).first()

    content = data['content']

    item = Item(content)

    a_list.items.append(item)

    db.session.add(a_list)
    db.session.add(item)
    db.session.commit()

    return '', 204  # no content

@csrf.exempt
@item_blueprint.route('/delete/<item_id>',methods=['POST'])
@login_required
def delete(item_id):

    item = Item.query.filter_by(id=item_id).first()

    if item:
        db.session.delete(item)
        db.session.commit()

    return '', 204 # no content
