from src.json_writters.json_stock_persister import JsonStockSerializer
from src.stock.inventory_good import InventoryGood
from src.stock.stock import Stock

import json

if __name__ == '__main__':
   
    stock = Stock()

    with JsonStockSerializer(stock, 'var/stock.json'):

        pasta = InventoryGood("pasta", "kg", 1.0)
        rice = InventoryGood("rice", "kg", 1.5)
        coffee = InventoryGood("coffee", "kg", 0.5)
        
        stock.add(pasta).add(rice).add(coffee)

    




