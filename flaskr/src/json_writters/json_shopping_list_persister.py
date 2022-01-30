from flaskr.src.common.persister import Persister
import json
import os
from flaskr.src.json_writters.json_shopping_item_encoder import ShoppingListEncoder
from flaskr.src.shopping.shopping_item import from_dict
from flaskr.db import get_db
from flask import session
from werkzeug.exceptions import abort

class JsonShoppingListSerializer(Persister):
    def __init__(self, item_list, file_path) -> None:
        super().__init__(item_list)
        self.file_path = file_path
    
    def load(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    self.load_stock_from_json(json_data=json.load(f))
        except ValueError as e:
            print('shopping list error')

    def load_stock_from_json(self, json_data):
        try:
            self.item_list.name = json_data['name']
            self.item_list.items = [from_dict(item_data=item) for item in json_data['items']]
        except ValueError as e:
            print('shopping list error')

    def persist(self):
        json_data = ShoppingListEncoder().encode(self.item_list)
        with open(self.file_path, 'w') as f:
            f.write(json_data)

class JsonShoppingListSerializerSQL(Persister):
    def __init__(self, item_list) -> None:
        super().__init__(item_list)
    
    def load(self, content: str ):
        self.load_stock_from_json(json_data=json.loads(content))

    def load_stock_from_json(self, json_data):
        try:
            self.item_list.name = json_data['name']
            self.item_list.items = [from_dict(item_data=item) for item in json_data['items']]
        except ValueError as e:
            print('loading stock error')

    def persist(self):
        

        json_data = ShoppingListEncoder().encode(self.item_list)
        print(json_data)

        db = get_db()
        db.execute(
            'UPDATE shopping_list SET content = ? '
            ' WHERE owner_id = ? AND list_name = ?',
            (json_data, session.get('user_id'), self.item_list.name,)
        )
        db.commit()
