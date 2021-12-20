from src.shopping.shopping_item import ShoppingItem
from src.common.items_list import ItemsList

class ShoppingListException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ShoppingList(ItemsList):
    def __init__(self, name, persister) -> None:
        if not name:
            raise ShoppingListException()
        super().__init__(items=[])
        self.name = name

    def add(self, item: ShoppingItem):
        self.items.append(item)

        return self

    def take(self, index: int) -> ShoppingItem:
        item = self.items[index]
        del self.items[index]

        return item
