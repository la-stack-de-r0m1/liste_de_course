from flask import Flask
from decouple import config

from flask import render_template

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = config('APP_SECRET_KEY')

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/shopping_list")
    def shopping_list():
        return render_template('shopping_list.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    from . import stock
    app.register_blueprint(stock.stock_bp)

    return app