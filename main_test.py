from src.json_writters.json_shopping_list_persister import JsonShoppingListSerializer
from src.shopping.shopping_item import ShoppingItem
from flaskr.src.shopping.shopping_list import ShoppingList
from flaskr.src.json_writters.json_stock_persister import JsonStockSerializer
from flaskr.src.stock.inventory_good import InventoryGood
from flaskr.src.stock.stock import Stock

if __name__ == '__main__':
   
    stock = Stock()
    with JsonStockSerializer(stock, 'var/stock.json'):
        pasta = InventoryGood("pasta", "kg", 1.0)
        rice = InventoryGood("rice", "kg", 1.5)
        coffee = InventoryGood("coffee", "kg", 0.5)
        stock.add(pasta).add(rice).add(coffee)

        shopping_list = ShoppingList('house')
        with JsonShoppingListSerializer(shopping_list, 'var/shopping_list.json'):
            pasta = ShoppingItem("pasta", "kg", 1.0)
            rice = ShoppingItem("rice", "kg", 1.0)
            coffee = ShoppingItem("coffee", "kg", 1.0)

            shopping_list.add(pasta).add(rice).add(coffee)
        







