# class Dog(Animal):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
#     def can_fly(self):
#         print('I believe I can fly')
#
# dog = Dog('Ted', 2)
# dog.can_fly()

class Dog:

    def __init__(self, name, age, mother=None, father=None):
        self.name = name
        self.age = age
        self.speed = 1.5
        self.mother = mother
        self.father = father

    @staticmethod
    def get_popular_breeds():
        return """
                  Labrador Retriever.
                  German Shepherd Dog.
                  Golden Retriever.
                  French Bulldog.
                  Bulldog."""

    def change_speed(self, new_speed):
        self.speed = new_speed

    def bark(self):
        print("bark bark!")

    def run(self, place):
        print(self.name, 'runs with speed ', self.speed, 'in', place)

    def bite(self, victim_name):
        print(self.name, 'bites', victim_name)

    # print all attributes of a dog
    def get_all_attributes(self):
        print("Dog's name is {}, it's age is {}, it runs with speed: {} km/h"
              .format(self.name, self.age, self.speed))

    def test(test):
        print("test")


print(Dog.get_popular_breeds())

dog = Dog("Reks", 2)
print(dog.get_popular_breeds())

print(dog.get_all_attributes())
# print(Dog.get_all_attributes())
print(Dog.get_all_attributes(dog))
