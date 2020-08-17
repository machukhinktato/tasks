class ItemDiscount:
    """ create class and his subclass, which will display
     parent attributes information, attributes will be encapsulated """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} {self.__price}'

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.get_name()} with price {self.get_price()} rubles'


if __name__ == '__main__':
    slot_1 = ItemDiscountReport('"Garmin 985"', 36306)
    print(slot_1.get_parent_data())
