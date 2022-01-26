from flask import (Flask, render_template, session)
from decouple import config

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = config('APP_SECRET_KEY')

    @app.route("/")
    def index():
        username = session['username'] if 'username' in session else None
        return render_template('index.html', username=username)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    from . import db
    db.init_app(app=app)

    from . import stock
    app.register_blueprint(stock.stock_bp)

    from . import shopping_list
    app.register_blueprint(shopping_list.shopping_list_bp)

    from . import auth
    app.register_blueprint(auth.auth_bp)

    return app