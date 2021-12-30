import unittest
from unittest.mock import MagicMock
from flaskr.src.stock.stock_service import StockService

class TestStockService(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        StockService.init_stock_serializer = MagicMock()
        StockService.save = MagicMock()

        self.service = StockService()

        return super().setUp()

    def test_form_validator(self):
        form_data = {
            'name': 'stuff',
            'unit': 'kg',
            'quantity': '3.5'
        }

        self.assertTrue(self.service.form_is_valid(form_data))

    def test_form_validator_error_empty_val(self):
        form_data = {
            'name': '',
            'unit': 'kg',
            'quantity': '3.5'
        }

        self.assertFalse(self.service.form_is_valid(form_data))

    def test_form_validator_error_missing_val(self):
        form_data = {
            'unit': 'kg',
            'quantity': '3.5'
        }

        self.assertFalse(self.service.form_is_valid(form_data))

    def test_form_validator_error_not_float_quantity_val(self):
        form_data = {
            'name': 'stuff',
            'unit': 'kg',
            'quantity': 'abc'
        }

        self.assertFalse(self.service.form_is_valid(form_data))

    def test_success_if_form_is_valid(self):
        form_data = {
            'name': 'stuff',
            'unit': 'kg',
            'quantity': '3.5'
        }

        messages = self.service.add(form_data=form_data)
        self.assertEqual({'category':'success', 'msg': 'good added!'}, messages)

    def test_error_if_form_is_not_valid(self):
        form_data = {
            'name': '',
            'unit': 'kg',
            'quantity': '3.5'
        }

        messages = self.service.add(form_data=form_data)
        self.assertEqual({'category':'error', 'msg': 'invalid form'}, messages)

    def test_save_stock_on_success(self):
        form_data = {
            'name': 'stuff',
            'unit': 'kg',
            'quantity': '3.5'
        }

        self.service.add(form_data=form_data)
        self.service.save.assert_called_once()