#1. % 100 21
#2. % 1000 12
#3.12 -> 21

# 12 % 10 * 10 + 12 // 10

number = int(input('Enter the checked number: '))
last_digits = number % 100
first_digits = number % 1000
first_digits = first_digits % 10 * 10 + 12 // 10
print(first_digits == last_digits)