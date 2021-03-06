from flaskr.src.shopping.shopping_list_controller import ShoppingListController
from flask import Blueprint
from flaskr.auth import login_required

shopping_list_bp = Blueprint('shopping_list', __name__, url_prefix='/shopping_list')

@shopping_list_bp.route("/", methods=['GET'])
@login_required
def shopping_list():
    controller = ShoppingListController()
    return controller.index()

@shopping_list_bp.route("/add", methods=['GET', 'POST'])
@login_required
def add():
    controller = ShoppingListController()
    return controller.add()

@shopping_list_bp.route("/del/<name>", methods=['GET', 'POST'])
@login_required
def delete(name):
    controller = ShoppingListController()
    return controller.delete(name)

@shopping_list_bp.route("/edit/<name>", methods=['GET', 'POST'])
@login_required
def edit(name):
    controller = ShoppingListController()
    return controller.edit(name)

@shopping_list_bp.route("/<name>", methods=['GET'])
@login_required
def show(name):
    controller = ShoppingListController()
    return controller.show(name)
