# Person adında klass yaratmaq gərəkir.
# Attributları full_name, email, unvan, cins, shexsiyyet vesiqesinin
# FIN kodu olacaq. Klassa attributları dəyişmək üçün metodlar
# əlavə edin

class Person():
    def __init__(self, full_name, gender, age, gmail, addres, ID_Cards):
        print('__init__ is called')
        self.full_name = full_name
        self.gender = gender
        self.age = age
        self.gmail = gmail
        self.addres = addres
        self.ID_Cards = ID_Cards

    def update_fullname(self, new_fullname):
        self.full_name = new_fullname

    # def __str__(self):
    #     return f'Person: fullname:{self.full_name}, gender:{self.gender}, ' \
    #            f'age:{self.age}, gmail:{self.gmail}, address:{self.addres}' \
    #            f'id_cards:{self.ID_Cards}'


person = Person("Ali Zeynalov", "Man", 27, "Ensteyn_guya.com", "Golden tomato Hotel", 5434543543)
# print("full_name", person.full_name)
# print("gender", person.gender)
# print("age", person.age)
# print("gmail", person.gmail)
# print("addres",person.addres)
# print("ID_Cards", person.ID_Cards)

print(person)
new_fullname = input('Enter new fullname:')
# person.full_name = new_fullname
person.update_fullname(new_fullname)

print(person)

