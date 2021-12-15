import unittest

from src.shopping.shopping_list import ShoppingList, ShoppingListException
from src.shopping.shopping_item import ShoppingItem

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

    def test_create_new_item_on_list(self):
        shopping_list = ShoppingList('Home')
        
        shopping_list.add(ShoppingItem('pasta', 42))
        item = shopping_list.items[0]

        self.assertEqual('pasta', item.name)
        self.assertEqual(42, item.quantity)

    def test_take_item_from_list(self):
        shopping_list = ShoppingList('Home')
        
        shopping_list.add(ShoppingItem('pasta', 42))
        shopping_list.add(ShoppingItem('rice', 21))
        item = shopping_list.take(0)

        self.assertEqual('pasta', item.name)
        self.assertEqual(42, item.quantity)

    def test_take_item_remove_from_list(self):
        shopping_list = ShoppingList('Home')
        
        shopping_list.add(ShoppingItem('pasta', 42))
        shopping_list.add(ShoppingItem('rice', 21))
        shopping_list.take(0)
        
        self.assertEqual(1, len(shopping_list.items))


