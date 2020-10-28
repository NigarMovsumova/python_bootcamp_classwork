from random import randint

length = 10
numbers = []
for i in range(length):
    numbers.append(randint(1, 99))
print(numbers)

for i in range(length - 1):
    for j in range(length - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
