from flask.helpers import url_for
from werkzeug.utils import redirect
from src.stock.stock_service import StockService
from flask import request, flash, render_template

class StockController:
    def __init__(self) -> None:
        self.service = StockService()
    
    def index(self):
        return render_template('stock.html', items=self.service.read())

    def add(self):
        messages = self.service.add(request.form) if request.method == 'POST' else None
        if messages:
            flash(message=messages['msg'], category=messages['category'])

        return render_template('stock_add.html', messages=messages)

    def edit(self, name):
        if request.method == 'GET':
            good = self.service.find_one(name)
            return render_template('stock_edit.html', good=good)
        elif request.method == 'POST':
            self.service.edit(request.form, name)
            flash(message='Quantité modifiée!', category='success')
            return redirect(url_for('stock'))

    def delete(self, name):
        if request.method == 'POST':
            self.service.delete(name)
        return redirect(url_for('stock'))
