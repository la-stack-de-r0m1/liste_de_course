import unittest
from src.stock.inventory_good import InventoryGood, from_dict
from src.common.item import CommonUnits

from src.common.exceptions import NegativeQuantityException, BadGoods

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
        self.rice += InventoryGood('rice', 'kg', 0.5)
        self.assertEqual(1.5, self.rice.quantity)

    def test_sub_operator(self):
        self.rice -= InventoryGood('rice', 'kg', 0.5)
        self.assertEqual(0.5, self.rice.quantity)

    def test_add_raises_on_different_good_type(self):
        with self.assertRaises(BadGoods) as ctx:
            self.rice += InventoryGood('flour', 'kg', 0.5)

    def test_sub_raises_on_different_good_type(self):
        with self.assertRaises(BadGoods) as ctx:
            self.rice -= InventoryGood('flour', 'kg', 0.5)

    def test_bad_instance_raise_exception(self):
        with self.assertRaises(BadGoods):
            self.rice += 1

    def test_load_inventoey_good_from_json(self):
        pasta_json = {'name': 'pasta', 'unit': 'kg', 'quantity': 1.5}
        good = from_dict(pasta_json)

        self.assertEqual('pasta', good.name)
        self.assertEqual('kg', good.unit)
        self.assertEqual(1.5, good.quantity)