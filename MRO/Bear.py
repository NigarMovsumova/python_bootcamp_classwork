# ayi klassinda qishda yatdigini bildiren metod var
# animal klassinda hemchinin hemin metod var.
from MRO.Animal import Animal


class Bear(Animal):
    def sleep_in_winter(self):
        print('I like to sleep during winter')


bear = Bear('Ahmad', 2, 'boz ayi')
animal = Animal('Doshan', 2, 'boz doshan')

bear.sleep_in_winter()
animal.sleep_in_winter()
