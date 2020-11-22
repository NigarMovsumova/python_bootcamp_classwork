from Dog import *
#  constructor
# adi, soyadi, vesiqe nomresi, iti var ya yox, dogum ili, vezifesi, shirketi

class Human:

    def __init__(self,
                 firstname,
                 lastname,
                 passport_id,
                 birthdate,
                 dog=None,
                 company=None,
                 position=None):
        self.firstname = firstname
        self.lastname = lastname
        self.passport_id = passport_id
        self.dog = dog
        self.birthdate = birthdate
        self.company = company
        self.position = position

    def get_all_attributes(self):
        print(self.firstname,
              self.lastname,
              self.passport_id,
              self.birthdate,
              self.company,
              self.position)
        if self.dog is not None:
            print(self.dog.name, self.dog.age)


human = Human('Nigar', 'Movsumova', 'tetetsts', '17-04-1994')
human.get_all_attributes()
# print(human.__getattribute__('lastname', 'firstname'))

maks = Dog('Maks', 8)
behlul = Human('Behlul', 'Mahmudlu', 'passport_id_example', '23-11-1995', maks)
behlul.get_all_attributes()





