class ItemDiscount:
    """ create class and his subclass, which will display
     parent attribute information """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.name} with price {self.price} rubles'


if __name__ == '__main__':
    a = ItemDiscountReport('"Garmin 985"', 36306)
    print(a.get_parent_data())
