import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


from markupsafe import escape

from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/regsiter', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not  password:
            error = 'Password is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered"
            else:
                return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route("/login", methods=['GET'])
def login_form():
    return render_template('auth/login.html')

@auth_bp.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    db = get_db()
    error = None

    user = db.execute(
        "SELECT * from user where username = ?", (username,)
    ).fetchone()

    if user is None:
        error = 'Cannot authenticate user'
    elif not check_password_hash(user['password'], password=password):
        error = 'Cannot authenticate user'

    if error is None:
        session.clear()
        session['user_id'] = user['id']

        return redirect(url_for('index'))
    
    flash(error)

    return render_template('auth/login.html')
        
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@auth_bp.before_app_request
def load_logged_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user where id = ?", (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view