# n reqemli ededin yalniz cut reqemlerini cemleyin

number = int(input('Enter the number: '))
counter = 0
# while number != 0:
#     # digit = number % 10
#     if number % 2 == 0:
#         counter += 1
#     number //= 10
# print(counter)

while number != 0:
    # digit = number % 10
    if number % 3 == 0:
        counter += 1
    number //= 10
print(counter)

