from json import JSONEncoder

class InventoryGoodEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__

class StockEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__
