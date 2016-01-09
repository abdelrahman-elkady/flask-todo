from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort

from app.config import csrf

from app.models import Item
from app.database import db

from flask.ext.login import login_required, current_user

item_blueprint = Blueprint(
    'item', __name__, template_folder='../templates/item')

@item_blueprint.route('/new', methods=['POST'])
@csrf.exempt
@login_required
def new():
    print request.get_json()

    return '', 204  # no content
