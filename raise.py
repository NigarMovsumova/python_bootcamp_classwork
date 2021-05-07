number = int(input('Enter a positive number: '))

if number < 0:
    raise Exception('number is negative.')