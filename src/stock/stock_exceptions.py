class StockException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NegativeQuantityException(StockException):
    def __init__(self, *args: object) -> None:
        super().__init__('Error: negative quantity')

class BadGoods(StockException):
    def __init__(self, *args: object) -> None:
        super().__init__('Error: Bad good types')