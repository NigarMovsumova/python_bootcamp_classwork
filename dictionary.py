import random

# Istifadechi key daxil edir. Eger o dictionaryde yoxdursa,
# hemin key elave edilir dictionaryye, value kimi ise her
# hansisa random ededi elave edirsiniz."

currencies = {
    "AZN": "Azerbaijan",
    "YTL": "Turkey",
    "RUBL": "Russia",
    "YUAN": "China",
    "EURO": ["Germany", 'France', 'Italy', 'Holland'],
}

dict_key = input('Enter a key:')

if dict_key not in currencies.keys():
    currencies[dict_key] = random.randint(0, 100)

print(currencies)
