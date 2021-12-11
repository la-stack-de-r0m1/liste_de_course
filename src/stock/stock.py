from src.stock.inventory_good import InventoryGood


class Stock:
    def __init__(self) -> None:
        self.goods = {}

    def total_quantity(self):
        return len(self.goods)

    def has(self, good_name):
        return good_name in self.goods

    def add(self, good):
        good_name = good.name
        if self.has(good_name):
            self.goods[good_name].quantity += good.quantity
        else:
            self.create_good(good)

    def create_good(self, good):
        self.goods[good.name] = good

    def get_quantity(self, good_name):
        return self.goods[good_name].quantity if self.has(good_name) else 0

    def take(self, good):
        returned_good = InventoryGood(good.name, good.unit, good.quantity)
        quantity = self.compute_new_quantity(returned_good) if self.has(good.name) else 0
        returned_good.quantity = quantity
    
        return returned_good

    def compute_new_quantity(self, good):
        quantity = good.quantity
        remaining_quantity = self.goods[good.name].quantity
        if remaining_quantity >= quantity:
            self.goods[good.name].quantity -= quantity
        else:
            quantity = remaining_quantity
            self.goods[good.name].quantity = 0
        return quantity