class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speed = 1.5

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


reks = Dog('Reks', 2)
max = Dog('Max', 1)

reks.bark()
reks.run('Baku')
reks.change_speed(10)
reks.run('Baku')
reks.bite('Nigar')
reks.run('Baku')
print(reks.name)
print(reks.speed)
print(reks.age)
reks.get_all_attributes()
# reks.test("test")
Dog.test('test')
Dog.get_all_attributes(reks)
Dog.get_all_attributes(max)
