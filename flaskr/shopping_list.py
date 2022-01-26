from flask import Blueprint
from flask.templating import render_template
from flaskr.auth import login_required
from flask import request

shopping_list_bp = Blueprint('shopping_list', __name__, url_prefix='/shopping_list')

@shopping_list_bp.route("/", methods=['GET'])
@login_required
def shopping_lists():
    return render_template("shopping_list/shopping_list.html")

@shopping_list_bp.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    return render_template('shopping_list/add.html')

