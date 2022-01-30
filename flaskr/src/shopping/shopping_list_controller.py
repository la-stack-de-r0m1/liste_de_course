from flask import request, flash,  render_template
from flaskr.src.shopping.shopping_list_service import ShoppingListService
from flask.helpers import url_for
from werkzeug.utils import redirect

class ShoppingListController():
    def __init__(self) -> None:
        pass

    def index(self):
        service = ShoppingListService()
        return render_template('shopping_list/shopping_list.html',
            items=service.read_all())

    def show(self, list_name):
        service = ShoppingListService()
        return render_template('shopping_list/show.html',
            item=service.show(list_name=list_name))

    def add(self):
        service = ShoppingListService()
        messages = service.add(request.form) if request.method == 'POST' else None
        if messages:
            flash(message=messages['msg'], category=messages['category'])
        return render_template('shopping_list/add.html', messages=messages)

    def delete(self, name):
        if request.method == 'POST':
            service = ShoppingListService()
            service.delete(name)
        return redirect(url_for('shopping_list.shopping_list'))

    def edit(self, name):
        service = ShoppingListService()
        if request.method == 'POST':
            item = service.edit(request.form, name)
        else:
            item = service.find_one(name)

        return render_template('shopping_list/edit.html', item=item)