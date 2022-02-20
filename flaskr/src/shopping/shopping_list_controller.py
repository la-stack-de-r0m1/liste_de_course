from flaskr.db import get_db
from flask import request, flash,  render_template, session
from flaskr.src.shopping.shopping_list_service import ShoppingListService
from flaskr.src.json_writters.json_shopping_list_persister import JsonShoppingListSerializerSQL
from flaskr.src.shopping.shopping_list_db import ShoppingListDb
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

class ShoppingListController():
    def __init__(self) -> None:
        db = ShoppingListDb(get_db())
        json_serializer = JsonShoppingListSerializerSQL(None)
        self.service = ShoppingListService(
            db=db,
            user_id=session.get('user_id'),
            list_serializer=json_serializer
        )

    def index(self):
        shopping_lists = self.service.read_all()
        if shopping_lists is None:
            abort(404, f"Shopping list cannot be loaded.")

        return render_template('shopping_list/shopping_list.html',
            items=shopping_lists)

    def show(self, list_name):
        return render_template('shopping_list/show.html',
            item=self.service.show(list_name=list_name))

    def add(self):
        messages = self.service.add(request.form) if request.method == 'POST' else None
        if messages:
            flash(message=messages['msg'], category=messages['category'])
        return render_template('shopping_list/add.html', messages=messages)

    def delete(self, name):
        if request.method == 'POST':
            self.service.delete(name)
        return redirect(url_for('shopping_list.shopping_list'))

    def edit(self, name):
        if request.method == 'POST':
            item = self.service.edit(request.form, name)
        else:
            item = self.service.find_one(name)

        return render_template('shopping_list/edit.html', item=item)