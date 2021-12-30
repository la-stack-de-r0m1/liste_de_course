import json
import unittest

from flaskr.src.stock.inventory_good import InventoryGood
from flaskr.src.stock.stock import Stock
from flaskr.src.json_writters.json_inventory_good_encoder import InventoryGoodEncoder, StockEncoder

class TestJSONEncoder(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.stock = Stock()
        pasta = InventoryGood('pasta', 'kg', 1.0)
        rice = InventoryGood('rice', 'kg', 1.5)
        coffee = InventoryGood('coffee','kg', 0.5)
        self.stock.add(pasta).add(rice).add(coffee)

        return super().setUp()

    def test_inventory_good_encode(self):
        rice = InventoryGood("rice", "kg", 1.0)
        json_data = InventoryGoodEncoder().encode(rice)
        self.assertEqual('{"name": "rice", "unit": "kg", "quantity": 1.0}', json_data)

    def test_inventory_good_encode_json_data(self):
        rice = InventoryGood("rice", "kg", 1.0)
        json_data = json.dumps(rice, indent=0, cls=InventoryGoodEncoder)
        self.assertEqual('{\n"name": "rice",\n"unit": "kg",\n"quantity": 1.0\n}', json_data)

    def test_stock_encode(self):
        json_data = StockEncoder().encode(self.stock)
        self.assertEqual('{"items": {"pasta": {"name": "pasta", "unit": "kg", "quantity": 1.0}, "rice": {"name": "rice", "unit": "kg", "quantity": 1.5}, "coffee": {"name": "coffee", "unit": "kg", "quantity": 0.5}}}',
            json_data)
