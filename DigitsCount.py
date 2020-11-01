# abcd - neche reqemin oldugunu tapmaq gerekir

# 123 // 10 - 12
# 123 % 10 - 3

from random import randint

number = randint(0, 200000)
print(number)


# 123 -> 0
# 123 // 10 = 12
# 12 // 10 = 1
# 1 // 10 = 0

def get_digits_count(number):
    digits_count = 0
    while number != 0:
        digits_count += 1
        number //= 10
    return digits_count


print(get_digits_count(number))
