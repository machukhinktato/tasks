class ItemDiscount:
    """ create class and his subclass, which will display
     parent attributes information, attributes will be encapsulated,
      subclass also could change attributes of parent and add self attribute,
      in additionaly there is attribute for discount and two subclasses with same function
      which shows polymorphism"""

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} price is: {self.__price}'

    def call_name(self):
        return self.__name

    def call_price(self, price=None):
        if price == None:
            return self.__price
        elif self.discount != 0:
            self.__price = price - self.discount
            return f'price with your discount - {self.__price}'
        else:
            self.__price = price
            return f'{self.__name} price is: {self.__price}'


class ItemDiscountReport_1(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = price / 100 * discount

    def __str__(self):
        if self.discount != 0:
            return f'price with your discount - {self.call_price() - self.discount}'
        else:
            return f'{self.call_price()}'

    def get_parent_data(self):
        return f'{self.call_name()} with price {self.call_price()} rubles'

    def get_info(self):
        return f'{self.call_name()}'


class ItemDiscountReport_2(ItemDiscount):

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = price / 100 * discount

    def __str__(self):
        if self.discount != 0:
            return f'price with your discount - {self.call_price() - self.discount}'
        else:
            return f'{self.call_price()}'

    def get_parent_data(self):
        return f'{self.call_name()} with price {self.call_price()} rubles'

    def get_info(self):
        return f'{self.call_price()}'


def value_handler(value):
    return value.get_info()


if __name__ == '__main__':
    slot_1 = ItemDiscountReport_1('"Garmin 985"', 36306, 10)
    slot_2 = ItemDiscountReport_2('"Garmin 985"', 36306, 10)
    # slot_1 = ItemDiscountReport_1('"Garmin 985"', 36306)
    # slot_2 = ItemDiscountReport_2('"Garmin 985"', 36306)
    print(f'primary option {slot_1.get_info()}')
    print(f'primary option {slot_2.get_info()}')
    for value in slot_1, slot_2:
        print(f'second option {value.get_info()}')
    print(f'third option {value_handler(slot_1)}')
    print(f'third option {value_handler(slot_2)}')
