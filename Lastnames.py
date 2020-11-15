lastnames = {
    'Nigar': 'Movsumova',
    'Alpay': 'Salahli',
    'Behlul': 'Mahmudlu',
    'Ilham': 'Sadikhov',
    'Nezrin': 'Jabbarli',
    'Ali': 'Abbasov',
    'Eldar': 'Eyvazov'
}

print(lastnames)

for pair in lastnames.items():
    print(pair)

for name in lastnames:
    print(name, lastnames[name])

for firstname, lastname in lastnames.items():
    print(firstname, lastname)

