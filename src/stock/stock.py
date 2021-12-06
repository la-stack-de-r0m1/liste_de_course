class Stock:

    def __init__(self) -> None:
        self.goods = {}

    def total_quantity(self):
        return len(self.goods)

    def has(self, good_name):
        return good_name in self.goods

    def add(self, good):
        good_name = good['name']
        if self.has(good_name):
            self.goods[good_name] += 1
        else:
            self.create_good(good_name)

    def create_good(self, good_name):
        self.goods[good_name] = 1

    def get(self, good_name):
        return self.goods[good_name] if self.has(good_name) else 0

    