class Cars:
    """A sample Cars class"""

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def type(self):
        return '{}.{}'.format(self.brand, self.model)

    def year_price(self):
        return '{} {}'.format(self.year, self.price)

    def __repr__(self):
        return "Car('{}', '{}', {}, {})".format(self.brand, self.model, self.year, self.price)
