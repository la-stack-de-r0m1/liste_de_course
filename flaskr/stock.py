from flask import Blueprint
from markupsafe import escape
from flaskr.src.stock.stock_controller import StockController

stock_controller = StockController()

stock_bp = Blueprint('stock', __name__, url_prefix='/stock')

@stock_bp.route("/")
def stock():
    return stock_controller.index()

@stock_bp.route("/add", methods=['POST', 'GET'])
def add():
    return stock_controller.add()

@stock_bp.route("/del/<name>", methods=['POST'])
def delete(name):
    name = escape(name)
    return stock_controller.delete(name)

@stock_bp.route("/<name>", methods=['POST', 'GET'])
def edit(name):
    name = escape(name)
    return stock_controller.edit(name)