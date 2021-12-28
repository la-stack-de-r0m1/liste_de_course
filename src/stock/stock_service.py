from src.json_writters.json_stock_persister import JsonStockSerializer
from src.stock.stock import Stock

class StockService:
    def __init__(self) -> None:
        self.stock = Stock()
        self.stock_serializer = JsonStockSerializer(self.stock, 'var/stock.json')
        self.stock_serializer.load()

    def save(self):
        self.stock_serializer.persist()

    def read(self):
        return self.stock.items

        
