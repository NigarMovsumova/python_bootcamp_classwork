# Istifadechi iki eded daxil edir.
# Onlarin biri birine bolunme neticesini
# chap etmek gerekir.

# try:
#     print(number / 0)
# except ZeroDivisionError:
#     print('You can not divide by zero.')

# 1. dividend, divider - istifadechi sehvi
# 2. 0-a bolme
# print(0 / 0)
# print(5 / 0)
# print(0 / 5)

# try:
#     dividend = int(input('Enter the dividend: '))
#     divider = int(input('Enter the divider: '))
#     print(dividend / divider)
# except ValueError:
#     print('You should enter a valid number.')
# except ZeroDivisionError:
#     print('You can not divide by zero.')

dividend = None
divider = None

try:
    dividend = int(input('Enter the dividend: '))
    divider = int(input('Enter the divider: '))
except ValueError:
    print('You should enter a valid number.')

try:
    print(dividend / divider)
except ZeroDivisionError:
    print('You can not divide by zero.')