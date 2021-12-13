import unittest

from src.shopping.shopping_list import ShoppingList, ShoppingListException

class TestShoppingList(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_shopping_list_name(self):
        shopping_list = ShoppingList('Home')
        self.assertEqual('Home', shopping_list.name)

    def test_raises_if_name_is_empty(self):
        with self.assertRaises(ShoppingListException):
            shopping_list = ShoppingList('')
