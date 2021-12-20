import unittest
from unittest.mock import MagicMock

from src.common.persister import Persister
from src.shopping.shopping_list import ShoppingList, ShoppingListException
from src.shopping.shopping_item import ShoppingItem


class TestShoppingList(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_shopping_list_name(self):
        shopping_list = ShoppingList('Home', None)
        self.assertEqual('Home', shopping_list.name)

    def test_raises_if_name_is_empty(self):
        with self.assertRaises(ShoppingListException):
            shopping_list = ShoppingList('', None)

    def test_create_new_item_on_list(self):
        shopping_list = ShoppingList('Home', None)
        
        shopping_list.add(ShoppingItem('pasta', '', 42))
        item = shopping_list.items[0]

        self.assertEqual('pasta', item.name)
        self.assertEqual(42, item.quantity)

    def test_take_item_from_list(self):
        shopping_list = ShoppingList('Home', None)
        
        shopping_list.add(ShoppingItem('pasta', '', 42))
        shopping_list.add(ShoppingItem('rice', '', 21))
        item = shopping_list.take(0)

        self.assertEqual('pasta', item.name)
        self.assertEqual(42, item.quantity)

    def test_take_item_remove_from_list(self):
        shopping_list = ShoppingList('Home', None)
        
        shopping_list.add(ShoppingItem('pasta', '', 42))
        shopping_list.add(ShoppingItem('rice', '', 21))
        shopping_list.take(0)
        
        self.assertEqual(1, len(shopping_list.items))

    # def test_persister_calls(self):
        # persister = Persister()
        # persister.load = MagicMock()
        # persister.persist = MagicMock()
# 
        # with ShoppingList('Home', persister) as shopping_list:
            # pass
# 
        # persister.load.assert_called_once()
#        persister.persist.assert_called_once()
