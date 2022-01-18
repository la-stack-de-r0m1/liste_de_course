from flask import Blueprint
from markupsafe import escape
from flaskr.src.stock.stock_controller import StockController
from flaskr.auth import login_required

#stock_controller = StockController()

stock_bp = Blueprint('stock', __name__, url_prefix='/stock')

@stock_bp.route("/")
@login_required
def stock():
    stock_controller = StockController()
    return stock_controller.index()

@stock_bp.route("/add", methods=['POST', 'GET'])
@login_required
def add():
    stock_controller = StockController()
    return stock_controller.add()

@stock_bp.route("/del/<name>", methods=['POST'])
@login_required
def delete(name):
    stock_controller = StockController()
    name = escape(name)
    return stock_controller.delete(name)

@stock_bp.route("/<name>", methods=['POST', 'GET'])
@login_required
def edit(name):
    stock_controller = StockController()
    name = escape(name)
    return stock_controller.edit(name)