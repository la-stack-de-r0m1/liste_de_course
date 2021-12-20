from src.common.persister import Persister

class ItemsList:
    def __init__(self, items) -> None:
        self.items = items

    def total_quantity(self):
        return len(self.items)