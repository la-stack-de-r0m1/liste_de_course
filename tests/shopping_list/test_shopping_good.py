import unittest
from src.shopping.shopping_item import ShoppingItem, NegativeQuantityException

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
            item = ShoppingItem('pasta', -1)