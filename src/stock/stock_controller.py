from flask import render_template
from src.stock.stock_service import StockService

class StockController:
    def __init__(self) -> None:
        self.service = StockService()
    
    def index(self):
        return render_template('stock.html', items=self.service.read())