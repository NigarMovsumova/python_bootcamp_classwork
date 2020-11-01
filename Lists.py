# 1. Lists
# liste reqemler elave edilir,
# o reqemlerin 10-dan ashagi olanlarini bir birine
# vurub neticeni qaytarmaq gerekir.

from random import randint


def calculate_product():
    numbers = []

    product = 1
    for i in range(5):
        numbers.append(randint(0, 5))
        if numbers[i] < 10:
            product *= numbers[i]
    print(product)


calculate_product()
