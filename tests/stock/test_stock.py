from src.stock.stock import Stock
from src.stock.inventory_good import InventoryGood
from src.json_writters.json_stock_persister import JsonStockSerializer

import unittest

class TestStock(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_empty_stock_on_startup(self):
        s = Stock()
        self.assertEqual(0, s.total_quantity())

    def test_add_good(self):
        s = Stock()
        
        s.add(InventoryGood('rice', 'kg', 1))
        print(s.items)

        self.assertEqual(1, s.total_quantity())

    def test_has_not_good(self):
        s = Stock()
        self.assertFalse(s.has('rice'))

    def test_has_good(self):
        s = Stock()
        s.add(InventoryGood('rice', 'kg', 1))
        self.assertTrue(s.has('rice'))

    def test_create_good(self):
        s = Stock()
        
        s.create_good(InventoryGood('rice', 'kg', 1))
        self.assertTrue(s.has('rice'))

        s.create_good(InventoryGood('flour', 'kg', 1))
        self.assertTrue(s.has('flour'))

    def test_count_rice_quantity_is_zero(self):
        s = Stock()
        
        nb_rice = s.get_quantity(good_name='rice')
        self.assertEqual(0, nb_rice)

    def test_count_rice_quantity(self):
        s = Stock()
        
        s.add(InventoryGood('rice', 'kg', 1))
        nb_rice = s.get_quantity(good_name='rice')
        self.assertEqual(1, nb_rice)

        s.add(InventoryGood('rice', 'kg', 1.5))
        nb_rice = s.get_quantity(good_name='rice')
        self.assertEqual(2.5, nb_rice)

    def test_add_rice(self):
        s = Stock()
        s.add(InventoryGood('rice', 'kg', 1))
        nb_rice = s.get_quantity(good_name='rice')
        self.assertEqual(1, nb_rice)

    def test_add_flour(self):
        s = Stock()
        s.add(InventoryGood('flour', 'kg', 1))
        nb_flour = s.get_quantity(good_name='flour')
        self.assertEqual(1, nb_flour)

    def test_remove_flour(self):
        s = Stock()
        s.add(InventoryGood('flour', 'kg', 2))

        nb_flour = s.get_quantity(good_name='flour')
        self.assertEqual(2, nb_flour)

        s.take(InventoryGood('flour', 'kg', 1))
        self.assertEqual(1, s.get_quantity(good_name='flour'))

    def test_stock_dont_go_negative(self):
        s = Stock()
        s.add(InventoryGood('flour', 'kg', 1))
        s.take(InventoryGood('flour', 'kg', 2))
        self.assertEqual(0, s.get_quantity(good_name='flour'))
        
    def test_taken_good(self):
        s = Stock()

        s.add(InventoryGood('flour', 'kg', 2))
        flour = s.take(InventoryGood('flour', 'kg', 0.5))
        self.assertEqual(0.5, flour.quantity)

    def test_empty_good_if_not_found(self):
        s = Stock()
        flour = s.take(InventoryGood('flour', 'kg', 0.5))
        self.assertEqual(0.0, flour.quantity)

    def test_load_stock_from_json(self):
        items = {
            "items": {
                "pasta": {"name": "pasta", "unit": "kg", "quantity": 1.0},
                "rice": {"name": "rice", "unit": "kg", "quantity": 1.5},
                "coffee": {"name": "coffee", "unit": "kg", "quantity": 0.5}
                }
            }

        s = Stock()
        p = JsonStockSerializer(s, '')
        p.load_stock_from_json(items)

        self.assertTrue(s.has('pasta'))
        self.assertEqual(1.0, s.get_quantity('pasta'))

        self.assertTrue(s.has('rice'))
        self.assertEqual(1.5, s.get_quantity('rice'))

        self.assertTrue(s.has('coffee'))
        self.assertEqual(0.5, s.get_quantity('coffee'))
