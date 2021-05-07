number = int(input('Enter the number: '))

try:
    print(number / 0)
except ZeroDivisionError:
    print('You can not divide by zero.')


