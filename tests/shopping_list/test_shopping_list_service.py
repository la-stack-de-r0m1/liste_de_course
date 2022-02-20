from flaskr.src.shopping.shopping_list import ShoppingList
from flaskr.src.shopping.shopping_list_db import ShoppingListDb
import unittest
from unittest.mock import MagicMock
from flaskr.src.shopping.shopping_list_service import ShoppingListService
from flaskr.src.json_writters.json_shopping_list_persister import JsonShoppingListSerializerSQL

class ShoppingListServiceTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        self.serializer = JsonShoppingListSerializerSQL(None)
        self.serializer.persist = MagicMock()

        self.db = ShoppingListDb(None)
        self.db.create_one = MagicMock()
        self.db.find_one_by = MagicMock(return_value={
            'list_name': 'test_name',
            'owner_id': 42,
            'content': '{"items": [{"name": "Patate", "unit": "kg", "quantity": 1.0}], "name": "test_name"}'
        })
        self.db.find_all_by_user =  MagicMock(return_value=[{
            'list_name': 'test_name',
            'owner_id': 42,
            'content': '{"items": [{"name": "Patate", "unit": "kg", "quantity": 1.0}], "name": "test_name"}'
        }])
        self.db.delete_one = MagicMock()
        self.db.update_list_name = MagicMock()

        self.list_service = ShoppingListService(db=self.db, user_id=42, list_serializer=self.serializer)

        return super().setUp()

    def test_ctor(self):
        s = ShoppingListService(db=self.db, user_id=42, list_serializer=self.serializer)
        self.assertEqual(s.db, self.db)
        self.assertEqual(42, s.user_id)
        self.assertEqual(s.list_serializer, self.serializer)

    def test_show(self):
        self.list_service.show('test_name')
        self.db.find_one_by.assert_called_once_with(42, 'test_name')

    def test_show_return_value(self):
        shopping_list = self.list_service.show('test_name')
        self.assertEqual('test_name', shopping_list.name)
        self.assertEqual('Patate', shopping_list.items[0].name)
        self.assertEqual('kg', shopping_list.items[0].unit)
        self.assertEqual(1.0, shopping_list.items[0].quantity)

    def test_find_all(self):
        self.list_service.read_all()
        self.db.find_all_by_user.assert_called_once_with(42)

    def test_find_all_return_value(self):
        shopping_lists = self.list_service.read_all()
        self.assertEqual('test_name', shopping_lists[0]['list_name'])
        self.assertEqual(42, shopping_lists[0]['owner_id'])
        self.assertEqual(
            '{"items": [{"name": "Patate", "unit": "kg", "quantity": 1.0}], "name": "test_name"}',
            shopping_lists[0]['content']
        )

    def test_add_success(self):
        result = self.list_service.add({'name': 'test_name'})
        self.db.create_one.assert_called_once_with(user_id=42, new_list_name='test_name')
        self.assertEqual('success', result["category"])
        self.assertEqual('List added!', result["msg"])

    def test_add_empty_name(self):
        result = self.list_service.add({'name': ''})
        self.db.create_one.assert_not_called()
        self.assertEqual('error', result["category"])
        self.assertEqual('List name cannot be empty', result["msg"])

    def test_add_exception(self):
        self.db.create_one = MagicMock(side_effect=Exception('boom'))
        result = self.list_service.add({'name': 'test_name'})
        self.assertEqual('error', result["category"])
        self.assertEqual('Cannot create list:boom', result["msg"])

    def test_delete(self):
        self.list_service.delete('list_name')
        self.db.delete_one.assert_called_once_with(42, 'list_name')

    def test_persist_item(self):
        self.list_service.persist_item(ShoppingList('test_name'))
        self.serializer.persist.assert_called_once()

    def test_is_valid(self):
        is_valid = self.list_service.is_valid({
            'name': 'test_name',
            'quantity': '1.0',
            'unit': 'kg'
        })
        self.assertTrue(is_valid)

    def test_is_not_valid(self):
        is_valid = self.list_service.is_valid({
            'name': '',
            'quantity': '',
            'unit': ''
        })
        self.assertFalse(is_valid)