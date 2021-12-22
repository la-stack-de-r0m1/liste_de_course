from json import JSONEncoder

from collections import namedtuple

class InventoryGoodEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__

class StockEncoder(JSONEncoder):
    def default(self, o: any) -> any:
        return o.__dict__
