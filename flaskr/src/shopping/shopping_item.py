from flaskr.src.common.item import Item

class ShoppingItem(Item):
    def __init__(self, name: str, unit: str = '', quantity: float = 1) -> None:
        super().__init__(name, unit, quantity)

def from_dict(item_data) -> ShoppingItem:
    return ShoppingItem(name=item_data['name'],
        unit=item_data['unit'],
        quantity=float(item_data['quantity']))