from flask import Flask
from decouple import config
from flask.helpers import url_for

from markupsafe import escape
from flask import render_template
from flask import session
from flask import request
from werkzeug.utils import redirect

def create_app(test_config=None):

    app = Flask(__name__)
    app.secret_key = config('APP_SECRET_KEY')

    @app.route("/")
    def index():
        username = session['username'] if 'username' in session else None
        return render_template('index.html', username=username)

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = escape(request.form['username'])
            return redirect(url_for('index'))
        else:
            return render_template('login_form.html')
            
    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('index'))


    @app.route("/shopping_list")
    def shopping_list():
        return render_template('shopping_list.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    from . import stock
    app.register_blueprint(stock.stock_bp)

    return app