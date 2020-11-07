# 3. 10 ölçülü kəsr ədədlərdən ibarət siyahi yaradın. Neçə rəqəmin
# kəsr hissəsinin olmadığını ekrana çıxaran program yazın. (məs: {12,
# 12.5, 10.1, 1,2} kəsr hissəsi olmayan ədədlər 3)

from random import *


# 4.0 - kəsr deyil
# 4.01 - kəsrdir
# 4 % 1 == 0

def count_decimals():
    decimals_count = 0
    numbers = []
    for i in range(0, 100):
        numbers.append(round(uniform(-30, 21), 2))
        if numbers[i] % 1 == 0:
            decimals_count += 1
    print(numbers)
    print(decimals_count)


count_decimals()
