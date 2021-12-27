from src.json_writters.json_shopping_item_encoder import ShoppingItemEncoder, ShoppingListEncoder
import unittest
from src.shopping.shopping_item import ShoppingItem
from src.shopping.shopping_list import ShoppingList

class TestShoppingListJsonEncoder(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.shopping_list = ShoppingList('home')
        pasta = ShoppingItem('pasta', 'kg', 1.0)
        rice = ShoppingItem('rice', 'kg', 1.5)
        coffee = ShoppingItem('coffee','kg', 0.5)
        self.shopping_list.add(pasta).add(rice).add(coffee)
        return super().setUp()

    def test_shopping_item_encode(self):
        rice = ShoppingItem("rice", "kg", 1.0)
        json_data = ShoppingItemEncoder().encode(rice)
        self.assertEqual('{"name": "rice", "unit": "kg", "quantity": 1.0}', json_data)

    def test_shopping_list_encode(self):
        json_data = ShoppingListEncoder().encode(self.shopping_list)
        self.assertEqual('{"items": [{"name": "pasta", "unit": "kg", "quantity": 1.0}, {"name": "rice", "unit": "kg", "quantity": 1.5}, {"name": "coffee", "unit": "kg", "quantity": 0.5}], "name": "home"}',
            json_data)
    