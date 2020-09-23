# 2 reqem daxil edilir. Onlarin bolme neticesi ekranda gosterilir.
# print(5/0)
# first = float(input('Enter the first number: '))

try:
    first = float(input('Enter the first number: '))
    second = float(input('Enter the second number: '))
except ValueError:
    print('Normal reqem daxil et')
else:
    try:
        print('Total result = ', first / second)
    except ZeroDivisionError as e:
        print(e, "Please try again")