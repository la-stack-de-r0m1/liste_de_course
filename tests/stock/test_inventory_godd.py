import unittest
from src.stock.inventory_good import InventoryGood, CommonUnits, NegativeQuantityException

class TestInventoryGood(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.rice = InventoryGood('rice', CommonUnits.KiloGram, 1.0)

        return super().setUp()

    def test_ctor(self):

        good = InventoryGood('rice', CommonUnits.KiloGram, 1.5)

        self.assertEqual(1.5, good.quantity)
        self.assertEqual(CommonUnits.KiloGram, good.unit)
        self.assertEqual('rice', good.name)

    def test_add_qty(self):
        self.rice.add(1.5)
        self.assertEqual(2.5, self.rice.quantity)

    def test_raise_exception_if_qty_negativ(self):
        with self.assertRaises(NegativeQuantityException) as ctx:
            self.rice.add(-1.0)

    def test_ctor_qty_is_positive(self):
        with self.assertRaises(NegativeQuantityException) as ctx:
            rice = InventoryGood('rice', CommonUnits.KiloGram, -42.0)

    def test_take_from_iventory(self):
        self.rice.take(0.5)
        self.assertEqual(0.5, self.rice.quantity)

    def test_take_quantity_is_positive(self):
        with self.assertRaises(NegativeQuantityException) as ctx:
           self.rice.take(-42.0)

    def test_the_actual_quantity_taken(self):
        taken_quantity = self.rice.take(0.5)
        self.assertEqual(0.5, taken_quantity)
        self.assertEqual(0.5, self.rice.quantity)

    def test_the_actual_quantity_taken_not_enough_supply(self):
        taken_quantity = self.rice.take(10)
        self.assertEqual(1.0, taken_quantity)
        self.assertEqual(0.0, self.rice.quantity)

    def test_add_operator(self):
        self.rice += InventoryGood('rive', 'kg', 0.5)
        self.assertEqual(1.5, self.rice.quantity)

    def test_sub_operator(self):
        self.rice -= InventoryGood('rive', 'kg', 0.5)
        self.assertEqual(0.5, self.rice.quantity)