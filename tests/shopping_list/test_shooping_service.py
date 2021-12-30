from flaskr.src.shopping.shopping_item import ShoppingItem
from flaskr.src.stock.inventory_good import InventoryGood
import unittest

from flaskr.src.shopping.shopping_service import ShoppingService
from flaskr.src.stock.stock import Stock
from flaskr.src.shopping.shopping_list import ShoppingList

class TestShoppingService(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.shopping_list = ShoppingList('Home')\
            .add(ShoppingItem('rice'))\
            .add(ShoppingItem('pasta'))\
            .add(ShoppingItem('eggs', '', 6))

        self.stock = Stock()\
            .add(InventoryGood('pasta', 'kg', 0.5))\
            .add(InventoryGood('rice', 'kg', 1.0))

        return super().setUp()

    def test_buy_item(self):
        shopping_service = ShoppingService(self.stock, self.shopping_list)
        shopping_item = self.shopping_list.items[1]

        shopping_service.buy(shopping_item)

        self.assertEqual(2, len(self.shopping_list.items))
        self.assertEqual(1.5, self.stock.get_quantity('pasta'))

    def test_buy_eggs(self):
        shopping_service = ShoppingService(self.stock, self.shopping_list)
        shopping_item = self.shopping_list.items[2]

        shopping_service.buy(shopping_item)

        self.assertEqual(2, len(self.shopping_list.items))
        self.assertEqual(6, self.stock.get_quantity('eggs'))