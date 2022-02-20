from flaskr.src.common.persister import Persister
from flaskr.src.shopping.shopping_list_db import ShoppingListDb
from flaskr.src.shopping.shopping_list import ShoppingList
from flaskr.src.shopping.shopping_item import from_dict

class ShoppingListService():
    def __init__(self,
                db: ShoppingListDb,
                user_id: int,
                list_serializer: Persister) -> None:
        self.db = db
        self.user_id = user_id
        self.list_serializer = list_serializer

    def show(self, list_name) -> ShoppingList:
        return self.find_one(list_name)

    def add(self, form_data):
        try:
            name = form_data['name']
            if name:
                self.db.create_one(user_id=self.user_id, new_list_name=name)
                return {'category':'success', 'msg': 'List added!'}
            else:
                return {'category':'error', 'msg': 'List name cannot be empty'} 
        except Exception as e:
            return {'category':'error', 'msg': 'Cannot create list:' + str(e)}

    def delete(self, name):
        self.db.delete_one(self.user_id, name)

    def edit(self, form_data, name):
        item = self.find_one(name)

        if 'add_new_button' in form_data and self.is_valid(form_data):
            new_item_on_list = from_dict(form_data)
            item.add(new_item_on_list)
            self.persist_item(item)

        if 'edit_button' in form_data and self.is_valid(form_data):
            index = [i for i, current_item in enumerate(item.items) if current_item.name == form_data['old_name']][0]
            if index != -1:
                item.take(index)
                item.add(from_dict(form_data))
                self.list_serializer.item_list = item
                self.list_serializer.persist()

        if 'delete_button' in form_data:
            index = [i for i, current_item in enumerate(item.items) if current_item.name == form_data['name']][0]
            if index != -1:
                item.take(index)
                self.persist_item(item)

        if 'rename_button' in form_data:
            self.db.update_list_name(
                user_id=self.user_id,
                old_name=form_data['old_name'],
                new_name=form_data['name']
            )
            item.name = form_data['name']
            self.persist_item(item)

        return item

    def find_one(self, list_name: str) -> ShoppingList:
        shopping_list = self.db.find_one_by(self.user_id, list_name)

        sl = ShoppingList(shopping_list['list_name'])
        self.list_serializer.item_list = sl
        self.list_serializer.load(content=shopping_list['content'])

        return sl

    def read_all(self) -> list:
        return self.db.find_all_by_user(self.user_id)

    def persist_item(self, item: ShoppingList) -> None:
        self.list_serializer.item_list = item
        self.list_serializer.persist()

    def is_valid(self, form_data):
        return len(form_data["name"]) \
            and len(form_data["quantity"]) \
            and len(form_data["unit"])
