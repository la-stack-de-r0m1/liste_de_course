from src.common.item import Item

class ShoppingItem(Item):
    def __init__(self, name: str, unit: str = '', quantity: float = 1) -> None:
        super().__init__(name, unit, quantity)
