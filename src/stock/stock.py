from src.common.persister import Persister
from src.stock.inventory_good import InventoryGood
from src.common.items_list import ItemsList

class Stock(ItemsList):
    def __init__(self, persister: Persister) -> None:
        super().__init__(items={})

    def add(self, good: InventoryGood):
        good_name = good.name
        if self.has(good_name):
            self.items[good_name] += good
        else:
            self.create_good(good)

        return self
    
    def has(self, good_name):
        return good_name in self.items

    def create_good(self, good):
        self.items[good.name] = good

    def get_quantity(self, good_name):
        return self.items[good_name].quantity if self.has(good_name) else 0

    def take(self, good: InventoryGood):
        returned_good = InventoryGood(good.name, good.unit, good.quantity)
        quantity = self.compute_new_quantity(returned_good) if self.has(good.name) else 0
        returned_good.quantity = quantity
    
        return returned_good

    def compute_new_quantity(self, good):
        quantity = good.quantity
        remaining_quantity = self.items[good.name].quantity
        if remaining_quantity >= quantity:
            self.items[good.name] -= good
        else:
            quantity = remaining_quantity
            self.items[good.name].quantity = 0
        return quantity