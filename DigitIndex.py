# ededde olan reqemleri tapiriq,
# sonra hansisa reqemin (mes. 6) hansi yerde oldugunu tapiriq

from random import randint

number = randint(0, 200000)
print(number)

digits_list = []

while number != 0:
    digits_list.append(number % 10)
    number //= 10

print(digits_list)

searched_digit = randint(0, 9)
print(searched_digit)
print(searched_digit in digits_list)

for i in range(len(digits_list)):
    if digits_list[i] == searched_digit:
        print(i)

# 1234 % 10 = 4
# 1234 // 10 = 123
#
# 123 % 10 = 3
# 123 // 10 = 12
#
# 12 % 10 = 2
# 12 // 10 = 1
#
# 1 % 10 = 1
# 1 // 10 = 0 - end
