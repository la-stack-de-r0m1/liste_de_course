class ItemException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NegativeQuantityException(ItemException):
    def __init__(self, *args: object) -> None:
        super().__init__('Error: negative quantity')

class BadGoods(ItemException):
    def __init__(self, *args: object) -> None:
        super().__init__('Error: Bad good types')