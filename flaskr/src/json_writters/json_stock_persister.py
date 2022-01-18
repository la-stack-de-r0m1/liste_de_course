import os
from flaskr.src.common.persister import Persister
import json
from flaskr.src.json_writters.json_inventory_good_encoder import StockEncoder
from flaskr.src.stock.inventory_good import from_dict
from flaskr.db import get_db
from flask import session
from werkzeug.exceptions import abort

def load_stock_from_json(json_data):
    items = json_data['items']
    inventory_goods = {}
    for k, v in items.items():
        inventory_goods[k] = from_dict(v)
    
    return inventory_goods

class JsonStockSerializer(Persister):
    def __init__(self, item_list, file_path) -> None:
        super().__init__(item_list)
        self.file_path = file_path
    
    def load(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    self.load_stock_from_json(json_data=json.load(f))
        except ValueError as e:
            print('loading stock error')

    def load_stock_from_json(self, json_data):
        try:
            self.item_list.items = load_stock_from_json(json_data=json_data)
        except ValueError as e:
            print('loading stock error')

    def persist(self):
        json_data = StockEncoder().encode(self.item_list)
        with open(self.file_path, 'w') as f:
            f.write(json_data)

class JsonStockSerializerFromSQL(Persister):
    def __init__(self, item_list) -> None:
        super().__init__(item_list)
    
    def load(self):
        user_stock = get_db().execute(
            'SELECT content'
            ' FROM stock '
            ' WHERE owner_id = ?',
            (session.get('user_id'),)
        ).fetchone()

        if user_stock is None:
            abort(404, f"Stock cannot be loaded.")
        
        self.load_stock_from_json(json_data=user_stock['content'])

    def load_stock_from_json(self, json_data):
        print(json_data)
        try:
            self.item_list.items = load_stock_from_json(json.loads(json_data))
        except ValueError as e:
            print('loading stock error')

    def persist(self):
        json_data = StockEncoder().encode(self.item_list)

        db = get_db()
        db.execute(
            'UPDATE stock SET content = ? '
            ' WHERE owner_id = ?',
            (json_data, session.get('user_id'))
        )
        db.commit()

