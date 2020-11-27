class CocaCola:

    def __init__(self, branding):
        self.__ingredients = ['Carbonated water', 'Sugar', 'Caffeine', 'Phosphoric acid v. caramel', 'coca leaf extract']
        self.branding = branding
        self.__price = 0.5

    def print(self):
        print(self.__ingredients, self.__price, self.branding)

    def update_price(self):
        self.__price = 0.8


ingredients = ['Carbonated water', 'Sugar', 'Caffeine', 'Phosphoric acid v. caramel', 'coca leaf extract']
cola = CocaCola(None)
#print(cola.__price)
#print(cola.price)

cola.print()
cola.update_price()
cola.print()

cola.price = 1000
cola.__price = 1000

cola.ingredients = None
cola.__ingredients = None

cola.branding = 'branding'

cola.print()
