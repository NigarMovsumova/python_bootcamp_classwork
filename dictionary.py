import random

# 1. Istifadechi key daxil edir. Eger o dictionaryde yoxdursa,
# hemin key elave edilir dictionaryye, value kimi ise her
# hansisa random ededi elave edirsiniz.

sample_dict = {
    'test': 1,
    'sample': 2
}

new_key = input('Enter new dict key: ')
if new_key in sample_dict.keys():
    print('The key is already in the dictionary.')
else:
    sample_dict[new_key] = random.randint(1, 10)
    print('New key is added')

print(sample_dict)
