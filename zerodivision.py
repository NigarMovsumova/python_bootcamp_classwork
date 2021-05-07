# number = int(input('Enter the number: '))
#
# try:
#     print(number / 0)
# except ZeroDivisionError:
#     print('You can not divide by zero.')


dividend = None
divider = None
try:
    dividend = int(input('Enter the dividend: '))
    divider = int(input('Enter the divider: '))
except ValueError:
    print('You should enter a valid number.')
else:
    try:
        print(dividend / divider)
    except ZeroDivisionError:
        print('You can not divide by zero.')