class Animal:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def can_fly(self, breed):
        if breed == 'dog':
            print('Dog can not fly')
        elif breed == 'bird':
            print('Birds can fly')
