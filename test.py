# is prime ?

# 2, 3, 5, 7

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 2, 3, 5, 7

# digit == 2, 3, 5, 7

number = int(input('Enter a number: '))

isPrime = True
for i in range(0, 5):
    digit = number % 10
    number = number /10
    if digit != 2 and digit != 3 and digit != 5 and digit != 7:
        isPrime = False
        print('All digits are not prime')
        break

if isPrime:
    print('All digits are prime')
