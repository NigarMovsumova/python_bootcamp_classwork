class Animal:

    def __init__(self, animal_type, breed, birth_date, area):
        self.animal_type = animal_type
        self.breed = breed
        self.birth_date = birth_date
        self.area = area

    def __str__(self):
        return 'Animal:\n type: {},\n breed:{},\n birth_date:{},\n area:{}\n'.format(
            self.animal_type, self.breed, self.birth_date, self.area)

    def who_am_i(self):
        print('I am a parent')


class Dog(Animal):

    def __init__(self, animal_type, breed, birth_date, area,
                 owner, name):
        super(Dog, self).__init__(animal_type, breed, birth_date,
                                  area)
        self.owner = owner
        self.name = name

    def __str__(self):
        return super(Dog, self).__str__() + \
               ' owner : {},\n name: {}\n' \
                   .format(self.owner, self.name)

    # def who_am_i(self):
    #     print('I am a child')


animal = Animal('fish', 'shark', '11.06.2021', 'Xezer')
animal.who_am_i()

dog = Dog('mamali', 'xaski', '11.06.2021', 'Torqovi',
          'Donald', 'Boris')
# print(dog)
dog.who_am_i()

# Human classin hansi metodlari ola bilerse, teyin edin.
# Employee class -> Human
