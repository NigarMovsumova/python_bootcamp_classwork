# 1. List verilir.
# Listin ichi doldurulur 10 eded random element elave edilir,
# onlar 0-5 araliginda ola bilerler.
# Bu funksiya sheklinde yazilmalidir.
# Listin ichinde hansisa ededi axtarib, onun indeksini qaytarmaq gerekir.
# Eger hemin eded listde yoxdursa, -1 qaytarin.
# buda hemchinin funskuta sheklinde yazilmalidir.

from random import randint


def create_randomized_list():
    numbers = []
    for i in range(0, 10):
        numbers.append(randint(0, 5))
    return numbers


def find_number(numbers, target):
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = create_randomized_list()
print(numbers)
print(find_number(numbers, 5))
