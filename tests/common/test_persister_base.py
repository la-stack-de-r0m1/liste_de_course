import unittest
from unittest.mock import MagicMock

from flaskr.src.common.persister import Persister

class PersisterTest(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_ctor(self):
        l = [1, 2]
        p = Persister(l)

        self.assertEqual(l, p.item_list)

    def test_load_data(self):
        loader = Persister([])
        loader.load = MagicMock()
        loader.persist = MagicMock()
        with loader as p:
            loader.load.assert_called_once()

    def test_save_data(self):
        loader = Persister([])
        loader.load = MagicMock()
        loader.persist = MagicMock()
        with loader as p:
            pass
        loader.persist.assert_called_once()