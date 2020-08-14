class ItemDiscount:
    """ create class and his subclass, which will display
     parent attributes information, attributes will be encapsulated,
      subclass also could change attributes of parent"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} {self.__price}'

    def call_name(self):
        return self.__name

    def call_price(self, price=None):
        if price == None:
            return self.__price
        else:
            self.__price = price
            return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.call_name()} with price {self.call_price()} rubles'


if __name__ == '__main__':
    slot_1 = ItemDiscountReport('"Garmin 985"', 36306)
    print(slot_1.get_parent_data())
    print(slot_1.call_price(37000))
    print(slot_1.get_parent_data())
