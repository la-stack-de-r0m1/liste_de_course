from json import JSONEncoder

class ShoppingItemEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__

class ShoppingListEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__