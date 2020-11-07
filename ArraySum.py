# 1. -30 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan
# massiv yaradın. Birinci müsbət ədəddən sonra gələn bütün rəqəmləri
# toplayan program yazın.

from random import *


def sum_list_elements():
    numbers = []
    sum = 0
    is_positive_found = False
    for i in range(0, 10):
        numbers.append(randint(-30, 21))
        if numbers[i] > 0:
            is_positive_found = True
        if is_positive_found:
            sum += numbers[i]
    print(numbers)
    print(sum)


sum_list_elements()
