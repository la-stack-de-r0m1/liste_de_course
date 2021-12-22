from src.common.persister import Persister
import json
from src.json_writters.json_inventory_good_encoder import StockEncoder

class JsonStockPersister(Persister):
    def __init__(self, item_list, file_path) -> None:
        super().__init__(item_list)
        self.file_path = file_path
        self.item = item_list
    
    def load(self):
        with open(self.file_path, 'r') as f:
            pass
            

    def persist(self):
        json_data = StockEncoder().encode(self.item)
        with open(self.file_path, 'w') as f:
            f.write(json_data)