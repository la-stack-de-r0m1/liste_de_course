import unittest
from flaskr.src.common.items_list import ItemsList

class ItemsListTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_items_is_none_on_startup(self):
        l = ItemsList()
        self.assertEqual(None, l.items)

    def test_items_len_is_null_on_startup(self):
        l = ItemsList()
        self.assertEqual(0, l.total_quantity())
    
    def test_items_len(self):
        l = ItemsList()
        l.items = [1, 2, 3]
        self.assertEqual(3, l.total_quantity())
