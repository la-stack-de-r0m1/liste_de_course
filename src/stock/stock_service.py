from src.stock.inventory_good import InventoryGood
from src.json_writters.json_stock_persister import JsonStockSerializer
from src.stock.stock import Stock

from markupsafe import escape

class StockService:
    def __init__(self) -> None:
        self.stock = self.create_stock()
        self.stock_serializer = self.create_stock_serializer()
        self.stock_serializer.load()

    def create_stock(self):
        return Stock()

    def create_stock_serializer(self):
        return JsonStockSerializer(self.stock, 'var/stock.json')

    def save(self):
        self.stock_serializer.persist()

    def read(self):
        return self.stock.items

    def add(self, form_data):
        if self.form_is_valid(form_data):
            good = InventoryGood(form_data['name'],
                form_data['unit'],
                float(form_data['quantity']))
            self.stock.add(good)
            self.save()

            return {'type':'success', 'msg': 'good added!'}

        return {'type':'error', 'msg': 'invalid form'}
    
    def form_is_valid(self, form_data):
        return form_data['name'] and form_data['unit'] and form_data['quantity']