string = 'Your height is {} and weight is {}'
weight = float(input('Enter the weight: '))
height = float(input('Enter the height: '))

print(string.format(height, weight))


#palindrom

#12345 - palindrom deyil
#12321 - palindromdur.

# 5 reqemlidir

number = int(input('Enter the checked number: '))

flag = False

# 12321 12 21 1 - 5, 2 - 4

# 12321 % 10 = 1
# 12321 / 10 = 1232
fifth_digit = number % 10
number = number // 10

# 1232 % 10 = 2
# 1232 / 10 = 123
forth_digit = number % 10
number //= 10

# 123 // 10 = 12
number //= 10

# 12 % 10 = 2
# 12 // 10 = 1
second_digit = number % 10
number //= 10

# 1 % 10 = 1
first_digit = number % 10

if fifth_digit == first_digit and second_digit == forth_digit:
    print(True)
else:
    print(False)





