import unittest
from src.shopping.shopping_item import ShoppingItem, from_dict
from src.common.item import NegativeQuantityException

class TestShoppingGood(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_shopping_item_name(self):
        item = ShoppingItem('pasta')
        self.assertEqual('pasta', item.name)
    
    def test_shopping_item_default_quantity(self):
        item = ShoppingItem('pasta')
        self.assertEqual(1, item.quantity)

    def test_raise_if_negative_quantity(self):
        with self.assertRaises(NegativeQuantityException):
            item = ShoppingItem('pasta', '',  -1)
    
    def test_load_item_from_json(self):
        pasta_json = {'name': 'pasta', 'unit': 'kg', 'quantity': 1.5}
        good = from_dict(pasta_json)

        self.assertEqual('pasta', good.name)
        self.assertEqual('kg', good.unit)
        self.assertEqual(1.5, good.quantity)