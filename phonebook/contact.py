class Contact:

    def __init__(self, name, number, workplace=None, address=None,
                 email=None, nickname=None):
        self.name = name
        self.number = number
        self.workplace = workplace
        self.address = address
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name}, {self.number})"

    def __str__(self):
        return f'{self.__class__.__name__} name={self.name}, number={self.number}'


# nigar = Contact('+994505532280', 'Nigar')
# zamin = Contact('+994505555555', 'Zamin')
# contact_list = [nigar, zamin]
# print(contact_list)
#
# nigar_str = repr(nigar)
#
# print(type(nigar_str))
#
# nigar_obj = eval(nigar_str)
# print(nigar_obj)
# print(type(nigar_obj))
# print(nigar_obj.name)
