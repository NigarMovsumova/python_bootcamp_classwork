class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        print('__add__ is called')
        print(self)
        print(other)
        print('*'*20)
        return BaseProduct("BaseProduct", self.price + other.price)

    # def test(self):
    #     print('I am a product')

    def __str__(self):
        return f'{self.name}, {self.price}'

# overriding
class Laptop(BaseProduct):
    pass
    # def test(self):
    #     print('I am a laptop')


class MobilePhone(BaseProduct):
    pass


samsung_note_10 = MobilePhone('Samsung Galaxy Note 10', 1000)
mac_pro = Laptop('Macbook Pro 16"', 3500)
nokia = MobilePhone("Nokia 3310", 50)

product_list = [samsung_note_10, mac_pro, nokia]



basket = samsung_note_10 + nokia + mac_pro
print('basket = ', basket)

# mac_pro.test()
# nokia.test()

