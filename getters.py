class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} (type = {self.type}, price = {self.price})'

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price})"


class Laptop(BaseProduct):
    pass


class MobilePhone(BaseProduct):
    pass

# total_price
class Basket:

    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, val):
        if type(val) in [MobilePhone, Laptop]:
            self.__iadd__(val)
        else:
            raise BasketSetterException(f'{type(val)} object can not be added to Basket.items')

    def __iadd__(self, product):
        self.__items.append(product)
        return self


class BasketSetterException(BaseException):
    pass

class Car:
    pass

samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)
car = Car()

basket = Basket()
print(basket.items)
basket.items = nokia
basket.items = nokia
basket.items = mac_pro
print(basket.items)
basket.items = car

# print(basket.items)
# basket.items = nokia
# print(basket.items)
# print(basket.items)
# basket.add(samsung_note_10)
# basket.add(nokia)
# basket.add(mac_pro)
# print(basket.items)
# basket.items.append(nokia)
# print(basket.items)
# basket.items = nokia

