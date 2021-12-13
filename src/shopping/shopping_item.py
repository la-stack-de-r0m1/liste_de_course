class NegativeQuantityException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__('Error: negative quantity')

class ShoppingItem:
    def __init__(self, name, quantity=1) -> None:
        if quantity < 0:
            raise NegativeQuantityException()

        self.name = name
        self.quantity = quantity