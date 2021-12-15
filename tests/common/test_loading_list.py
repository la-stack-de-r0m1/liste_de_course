from src.common.item import CommonUnits
from src.common.loading_list import LoadingList
from src.common.persister import Persister

import unittest
from unittest.mock import MagicMock

class TestLoadingList(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)

    def setUp(self) -> None:
        return super().setUp()

    def test_persister_calls(self):
        persister = Persister()
        persister.load = MagicMock()
        persister.persist = MagicMock()

        with LoadingList(persister) as loading_list:
            pass 

        persister.load.assert_called_once()
        persister.persist.assert_called_once()