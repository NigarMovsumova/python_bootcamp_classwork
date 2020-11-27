from MRO.Animal import Animal
from MRO.HumanFriend import HumanFriend


class Dog(Animal, HumanFriend):
    def eat_humans(self):
        print('Are you crazy? They are my friends <3')


dog = Dog('Richard', 2, 'pitbull')
print(dog)
dog.eat_humans()
