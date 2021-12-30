from flaskr.src.stock.inventory_good import InventoryGood

class ShoppingService:
    def __init__(self, stock, shopping_list) -> None:
        self.stock = stock
        self.shopping_list = shopping_list

    def buy(self, item):
        item_index = self.shopping_list.items.index(item)
        shopping_item = self.shopping_list.take(item_index)
        self.stock.add(InventoryGood(shopping_item.name, shopping_item.unit, shopping_item.quantity))