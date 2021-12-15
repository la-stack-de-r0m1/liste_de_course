from src.common.exceptions import BadGoods, NegativeQuantityException
from src.common.item import Item

def is_positive(func):
    def inner(self, quantity: float):
        if quantity < 0:
            raise NegativeQuantityException()
        return func(self, quantity)
    return inner

def type_verif(func):
    def inner(self, other):
        if not isinstance(other, type(self)) or self.name != other.name:
            raise BadGoods()
        return func(self, other)
    return inner

class InventoryGood(Item):
    def __init__(self, name: str, unit: str, quantity: float) -> None:
       super().__init__(name, unit, quantity)

    @type_verif
    def __add__(self, other):
        self.add(other.quantity)
        return self

    @type_verif
    def __sub__(self, other):
        self.take(other.quantity)
        return self

    @is_positive
    def add(self, quantity: float):
        self.quantity += quantity

    @is_positive
    def take(self, quantity: float):
        taken_quatity = quantity
        if quantity > self.quantity:
            taken_quatity = self.quantity
            self.quantity = 0
        else:
            self.quantity -= quantity

        return taken_quatity

    
