from flaskr.src.shopping.shopping_list import ShoppingList
from flaskr.db import get_db
from flask import session
from werkzeug.exceptions import abort
from flaskr.src.json_writters.json_shopping_list_persister import JsonShoppingListSerializerSQL
from flaskr.src.shopping.shopping_item import from_dict

class ShoppingListService():
    def __init__(self) -> None:
        pass

    def read_all(self):
        user_shopping_list = get_db().execute(
            'SELECT id, list_name'
            ' FROM shopping_list '
            ' WHERE owner_id = ?',
            (session.get('user_id'),)
        ).fetchall()

        if user_shopping_list is None:
            abort(404, f"Shopping list cannot be loaded.")

        return user_shopping_list

    def show(self, list_name):
        return self.find_one(list_name)

    def add(self, form_data):
        try:
            db = get_db()
            name = form_data['name']
            if name:
                owner_id = session.get('user_id')
                content = '{"items":[], "name": "' + name + '" }'
                db.execute(
                    "INSERT INTO shopping_list (owner_id, content, list_name) VALUES (?, ?, ?)",
                    (owner_id, content, name),
                    )
                db.commit()
                return {'category':'success', 'msg': 'List added!'}
            else:
                return {'category':'error', 'msg': 'List name cannot be empty'}    
        except Exception as e:
            return {'category':'error', 'msg': 'Cannot create list:' + str(e)}

    def delete(self, name):
        owner_id = session.get('user_id')
        db = get_db()
        db.execute(
            "DELETE FROM shopping_list WHERE owner_id = ? AND list_name = ?",
            (owner_id, name),
        )
        db.commit()

    def edit(self, form_data, name):
        item = self.find_one(name)

        if form_data["name"] and form_data["quantity"] and form_data["unit"]:
            new_item_on_list = from_dict(form_data)
            item.add(new_item_on_list)

            slsql = JsonShoppingListSerializerSQL(item)
            slsql.persist()

        return item

    def find_one(self, name):
        shopping_list = get_db().execute(
            'SELECT * '
            ' FROM shopping_list '
            ' WHERE owner_id = ? AND list_name = ?',
            (session.get('user_id'), name,)
        ).fetchone()

        sl = ShoppingList(shopping_list['list_name'])
        slsql = JsonShoppingListSerializerSQL(sl)
        slsql.load(content=shopping_list['content'])

        return sl

