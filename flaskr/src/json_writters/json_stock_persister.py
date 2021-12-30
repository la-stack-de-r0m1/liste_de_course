import os
from flaskr.src.common.persister import Persister
import json
from flaskr.src.json_writters.json_inventory_good_encoder import StockEncoder
from flaskr.src.stock.inventory_good import from_dict

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
            items = json_data['items']
            inventory_goods = {}
            for k, v in items.items():
                inventory_goods[k] = from_dict(v)
            self.item_list.items = inventory_goods
        except ValueError as e:
            print('loading stock error')

    def persist(self):
        json_data = StockEncoder().encode(self.item_list)
        with open(self.file_path, 'w') as f:
            f.write(json_data)