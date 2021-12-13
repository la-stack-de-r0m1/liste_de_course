from src.shopping.shopping_item import ShoppingItem

class ShoppingListException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ShoppingList:
    def __init__(self, name) -> None:
        if not name:
            raise ShoppingListException()
        self.name = name