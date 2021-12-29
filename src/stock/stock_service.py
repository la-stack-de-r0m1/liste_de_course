from app import stock
from src.stock.inventory_good import InventoryGood
from src.json_writters.json_stock_persister import JsonStockSerializer
from src.stock.stock import Stock

class StockService:
    def __init__(self) -> None:
        self.stock = self.create_stock()
        self.stock_serializer = self.init_stock_serializer()

    def create_stock(self):
        return Stock()

    def init_stock_serializer(self):
        stock_serializer = JsonStockSerializer(self.stock, 'var/stock.json')
        stock_serializer.load()
        return stock_serializer

    def save(self):
        self.stock_serializer.persist()

    def read(self):
        return self.stock.items

    def add(self, form_data):
        if self.form_is_valid(form_data):
            self.create_and_add_good(form_data)
            return {'category':'success', 'msg': 'good added!'}
        else:
            return {'category':'error', 'msg': 'invalid form'}
    
    def create_and_add_good(self, form_data):
        good = InventoryGood(form_data['name'],
            form_data['unit'],
            float(form_data['quantity']))
        self.stock.add(good)
        self.save()

    def form_is_valid(self, form_data):
        if 'name' in form_data and 'unit' in form_data and 'quantity' in form_data:
            try:
                float(form_data['quantity'])
            except ValueError:
                return False
    
            return form_data['name'] and form_data['unit'] and form_data['quantity']
        else:
            return False

    def find_one(self, name):
        return self.stock.items[name] if self.stock.has(name) else None

    def edit(self, form_data, name):
        good = self.find_one(name)
        if good:
            good.quantity = form_data["quantity"]
            self.save()

    def delete(self, name):
        good = self.find_one(name)
        if good:
            del self.stock.items[name]
            self.save()
        