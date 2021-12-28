from flask import render_template
from src.stock.stock_service import StockService
from flask import request

class StockController:
    def __init__(self) -> None:
        self.service = StockService()
    
    def index(self):
        return render_template('stock.html', items=self.service.read())

    def add(self):
        messages = self.service.add(request.form) if request.method == 'POST' else None
        return render_template('stock_add.html', messages=messages)