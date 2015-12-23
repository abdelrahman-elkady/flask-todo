from flask import Blueprint,  render_template, redirect, url_for, request, flash, abort
from app.models import List
from app.database import db

from flask.ext.login import login_required, current_user

list_blueprint = Blueprint(
    'list', __name__, template_folder='../templates/user')
