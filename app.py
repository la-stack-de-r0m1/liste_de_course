from src.stock.stock_controller import StockController
from flask import Flask
from decouple import config
from markupsafe import escape

from flask import render_template

app = Flask(__name__)
app.secret_key = config('APP_SECRET_KEY')
s = StockController()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stock")
def stock():
    return s.index()

@app.route("/stock/add", methods=['POST', 'GET'])
def add():
    return s.add()

@app.route("/stock/del/<name>", methods=['POST'])
def delete(name):
    name = escape(name)
    return s.delete(name)

@app.route("/stock/<name>", methods=['POST', 'GET'])
def edit(name):
    name = escape(name)
    return s.edit(name)

@app.route("/shopping_list")
def shopping_list():
    return render_template('shopping_list.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404