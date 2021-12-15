from src.shopping.shopping_item import ShoppingItem

class ShoppingListException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ShoppingList:
    def __init__(self, name) -> None:
        if not name:
            raise ShoppingListException()
        self.name = name
        self.items = []

    def add(self, item: ShoppingItem):
        self.items.append(item)

        return self

    def take(self, index: int) -> ShoppingItem:
        item = self.items[index]
        del self.items[index]

        return item
