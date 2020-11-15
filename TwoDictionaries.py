dict_az = {
    'My age is': 'Mənim {} yaşım var'
}

dict_ru = {
    'My age is': 'Мне {} лет'
}

if 'My age is' in dict_az:
    print(dict_az['My age is'].format(17))

if 'My age is' in dict_ru:
    print(dict_ru['My age is'].format(17))
