# factorial
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 2! = 1 * 2

# factorial = 1
# number = 5
# factorial = factorial * 1
# factorial = factorial * 2 = 2
# factorial = factorial * 3 = 6
# factorial = factorial * 4 = 24
# factorial = factorial * 5 = 120

number = int(input('Enter the number: '))
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)
