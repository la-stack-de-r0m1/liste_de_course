from dataclasses import dataclass
from enum import Enum
from flaskr.src.common.exceptions import NegativeQuantityException

class CommonUnits(Enum):
    NumberOf = "",
    KiloGram = "kg",
    Gram = "g"

@dataclass
class Item:
    name: str
    quantity: float
    unit: str

    def __init__(self, name: str, unit: str = '', quantity: float = 1) -> None:
        if quantity < 0:
            raise NegativeQuantityException()

        self.name = name
        self.unit = unit
        self.quantity = quantity