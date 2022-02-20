import unittest
from unittest.mock import MagicMock
from flaskr.src.shopping.shopping_list_db import ShoppingListDb

class FakeCursor():
    def fetchone(self):
        return {}

    def fetchall(self):
        return []

class FakeDb:
    def execute(self, query: str):
        return self.c

    def commit(self):
        pass

class ShoppingListDbTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_ctor(self):
        db = ShoppingListDb("db_conn")
        self.assertEqual("db_conn", db.db_object)

    def test_find_one_execute(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock(return_value=FakeCursor())
        
        db = ShoppingListDb(db_conn)
        db.find_one_by(user_id=42, list_name="test_list_name")

        db_conn.execute.assert_called_once_with(
             'SELECT * '
            ' FROM shopping_list '
            ' WHERE owner_id = ? AND list_name = ?',
            (42, "test_list_name",)
        )

    def test_find_one_fetchone(self):
        db_conn = FakeDb()
        c = FakeCursor()
        c.fetchone = MagicMock(return_value={})
        db_conn.execute = MagicMock(return_value=c)

        db = ShoppingListDb(db_conn)
        db.find_one_by(user_id=42, list_name="test_list_name")
        
        c.fetchone.assert_called_once()

    def test_find_all_execute(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock(return_value=FakeCursor())

        db = ShoppingListDb(db_conn)
        db.find_all_by_user(42)

        db_conn.execute.assert_called_once_with(
            'SELECT id, list_name'
            ' FROM shopping_list '
            ' WHERE owner_id = ?',
            (42,)
        )

    def test_find_all_fetchall(self):
        db_conn = FakeDb()
        c = FakeCursor()
        c.fetchall = MagicMock(return_value=[])
        db_conn.execute = MagicMock(return_value=c)

        db = ShoppingListDb(db_conn)
        db.find_all_by_user(42)

        c.fetchall.assert_called_once()

    def test_delete_execute(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()

        db = ShoppingListDb(db_conn)
        db.delete_one(user_id=42, list_name="test_list_name")

        db_conn.execute.assert_called_once_with(
             "DELETE FROM shopping_list WHERE owner_id = ? AND list_name = ?",
            (42, "test_list_name"),
        )

    def test_delete_commit(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()
        db_conn.commit = MagicMock()

        db = ShoppingListDb(db_conn)
        db.delete_one(user_id=42, list_name="test_list_name")

        db_conn.commit.assert_called_once()

    def test_update_execute(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()

        db = ShoppingListDb(db_conn)
        db.update_list_name(user_id=42, old_name="old", new_name="new")

        db_conn.execute.assert_called_once_with(
             'UPDATE shopping_list SET list_name = ? '
            ' WHERE owner_id = ? AND list_name = ?',
            ("new", 42, "old",)
        )

    def test_update_commit(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()
        db_conn.commit = MagicMock()

        db = ShoppingListDb(db_conn)
        db.update_list_name(user_id=42, old_name="old", new_name="new")

        db_conn.commit.assert_called_once()

    def test_create_one_execute(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()

        db = ShoppingListDb(db_conn)
        db.create_one(user_id=42, new_list_name="new")
        db_conn.execute.assert_called_once_with(
            
              "INSERT INTO shopping_list (owner_id, content, list_name) VALUES (?, ?, ?)",
               (42, '{"items":[], "name": "new" }', "new"),
        )

    def test_create_one_commit(self):
        db_conn = FakeDb()
        db_conn.execute = MagicMock()
        db_conn.commit = MagicMock()

        db = ShoppingListDb(db_conn)
        db.create_one(user_id=42, new_list_name="new")

        db_conn.commit.assert_called_once()