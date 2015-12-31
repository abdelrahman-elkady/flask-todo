from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort

from app.models import Item
from app.database import db

from flask.ext.login import login_required, current_user

item_blueprint = Blueprint(
    'item', __name__, template_folder='../templates/item')

@item_blueprint.route('/',methods=['GET'])
@login_required
def index():

    items = Item.query.all()

    return render_template('new.html')
