from flask import request, flash,  render_template
from flaskr.src.shopping.shopping_list_service import ShoppingListService

class ShoppingListController():
    def __init__(self) -> None:
        pass

    def index(self):
        service = ShoppingListService()
        return render_template('shopping_list/shopping_list.html',
            items=service.read_all())

    def add(self):
        service = ShoppingListService()
        messages = service.add(request.form) if request.method == 'POST' else None
        if messages:
            flash(message=messages['msg'], category=messages['category'])
        return render_template('shopping_list/add.html', messages=messages)