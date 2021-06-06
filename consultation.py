# İstifadəçi ədəd daxil edir, bu ədədin rəqəmlərinin
# artan ardıcıllıqla olub olmamasını
# yoxlayan proqram yazın.(12299 artan ardıcıllıq, 122044 artan ardıcıllıq deyil)

# number = int(input('Enter the number: '))
# flag = True
# while number != 0:
#     previous_digit = number % 10
#     current_digit = number % 100 // 10
#     if current_digit > previous_digit:
#         flag = False
#         break
#     number //= 10
#
# print(flag)


# 2) İstifadəçi istənilən sayda rəqəmli ədəd daxil edir,
# ədədi əksinə çevirən proqram yazın.
# 12345
# 54321
import math

number = int(input('Enter the number: '))
digit_counter = 0
number_copy = number
while number_copy != 0:
    digit_counter += 1
    number_copy //= 10


result_number = 0
while number != 0:
    digit = number % 10
    result_number += digit * math.pow(10, digit_counter - 1)
    digit_counter -= 1
    number //= 10

print(int(result_number))

# 1234 -> 4321
# 4 * 1000 + 3 * 100 + 2 * 10 + 1
# 10 ^ 3 - 10 ^ (reqemlerin sayi)

# 12345 -> 54321
# 5 * 10000 + 4 * 1000 ...

