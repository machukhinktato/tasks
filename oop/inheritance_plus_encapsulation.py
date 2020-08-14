class ItemDiscount:
    """ create class and his subclass, which will display
     parent attributes information, attributes will be encapsulated """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} {self.__price}'


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'{self.__name} with price {self.__price} rubles'


if __name__ == '__main__':
    slot_1 = ItemDiscountReport('"Garmin 985"', 36306)
    try:
        print(slot_1.get_parent_data())
    except:
        print("AttributeError: 'ItemDiscountReport' object"
              " has no attribute '_ItemDiscountReport__name'")
    # print(slot_1.get_parent_data())
    # slot_2 = ItemDiscount('"Garmin 985"', 36306)
    # print(slot_2._ItemDiscount__name, slot_2._ItemDiscount__price)
    # print(slot_2.__name, slot_2.__price)
