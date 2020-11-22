#  constructor
# adi, soyadi, vesiqe nomresi, iti var ya yox, dogum ili, vezifesi, shirketi

class Human:

    def __init__(self,
                 firstname,
                 lastname,
                 passport_id,
                 birthdate,
                 has_dog=False,
                 company=None,
                 position=None):
        self.firstname = firstname
        self.lastname = lastname
        self.passport_id = passport_id
        self.has_dog = has_dog
        self.birthdate = birthdate
        self.company = company
        self.position = position

    def get_all_attributes(self):
        print(self.firstname, self.lastname, self.passport_id, self.birthdate, self.has_dog, self.company,
              self.position)


human = Human('Nigar', 'Movsumova', 'tetetsts', '17-04-1994')
human.get_all_attributes()

