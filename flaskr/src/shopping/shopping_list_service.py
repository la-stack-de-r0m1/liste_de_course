from flaskr.db import get_db
from flask import session
from werkzeug.exceptions import abort

class ShoppingListService():
    def __init__(self) -> None:
        pass

    def read_all(self):
        user_shopping_list = get_db().execute(
            'SELECT id, name'
            ' FROM shopping_list '
            ' WHERE owner_id = ?',
            (session.get('user_id'),)
        ).fetchall()

        if user_shopping_list is None:
            abort(404, f"Shopping list cannot be loaded.")

    def add(self, form_data):
        try:
            db = get_db()
            name = form_data['name']
            owner_id = session.get('user_id')
            db.execute(
                "INSERT INTO shopping_list (owner_id, content, list_name) VALUES (?, ?, ?)",
                (owner_id, "", name),
                )
            db.commit()
            return {'category':'success', 'msg': 'List added!'}
        except Exception as e:
            return {'category':'error', 'msg': 'Cannot create list'}