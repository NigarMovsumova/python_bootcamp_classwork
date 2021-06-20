class Person:
    def __init__(self, name):
        self.name = name

    def update_name(self, name):
        self.name = name


person = Person('Murad')
person.update_name('Shahhuseyn')
