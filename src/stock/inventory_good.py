from dataclasses import dataclass
from enum import Enum

class CommonUnits(Enum):
    NumberOf = ''
    KiloGram = 'kg',
    Gram = 'g'

class NegativeQuantityException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def is_positive(func):
    def inner(self, quantity: float):
        if quantity < 0:
            raise NegativeQuantityException()
        return func(self, quantity)
    return inner

@dataclass
class InventoryGood:
    name: str
    unit: str
    quantity: float = 0.0

    def __init__(self, name: str, unit: str, quantity: float) -> None:
        if quantity < 0:
            raise NegativeQuantityException()

        self.name = name
        self.unit = unit
        self.quantity = quantity

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

    
