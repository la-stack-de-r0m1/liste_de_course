from src.stock.stock_controller import StockController
from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stock")
def stock():
    s = StockController()
    return s.index()

@app.route("/shopping_list")
def shopping_list():
    return render_template('shopping_list.html')
