from src.stock.stock import Stock
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
        s.add({'name': 'rice'})

        self.assertEqual(1, s.total_quantity())

    def test_has_not_good(self):
        s = Stock()
        self.assertFalse(s.has('rice'))

    def test_has_good(self):
        s = Stock()
        s.add({'name': 'rice'})
        self.assertTrue(s.has('rice'))

    def test_create_good(self):
        s = Stock()
        
        s.create_good('rice')
        self.assertTrue(s.has('rice'))

        s.create_good('flour')
        self.assertTrue(s.has('flour'))

    def test_count_rice_quantity_is_zero(self):
        s = Stock()
        
        nb_rice = s.get(good_name='rice')
        self.assertEqual(0, nb_rice)

    def test_count_rice_quantity(self):
        s = Stock()
        
        s.add({'name': 'rice'})
        nb_rice = s.get(good_name='rice')
        self.assertEqual(1, nb_rice)

        s.add({'name': 'rice'})
        nb_rice = s.get(good_name='rice')
        self.assertEqual(2, nb_rice)

    def test_add_rice(self):
        s = Stock()
        s.add({'name': 'rice'})
        nb_rice = s.get(good_name='rice')
        self.assertEqual(1, nb_rice)

    def test_add_flour(self):
        s = Stock()
        s.add({'name': 'flour'})
        nb_flour = s.get(good_name='flour')
        self.assertEqual(1, nb_flour)

    def test_remove_flour(self):
        s = Stock()
        s.add({'name': 'flour'})

        nb_flour = s.get(good_name='flour')
        self.assertEqual(1, nb_flour)

        s.take('flour')
        self.assertEqual(0, s.get(good_name='flour'))

    def test_stock_dont_go_negative(self):
        s = Stock()
        s.add({'name': 'flour'})
        s.take('flour')
        s.take('flour')
        self.assertEqual(0, s.get(good_name='flour'))
        
