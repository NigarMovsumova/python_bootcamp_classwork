from random import randint

length = 10
numbers = []
for i in range(length):
    numbers.append(randint(1, 99))
print(numbers)

i = 0
while i < length - 1:
    j = 0
    while j < length - 1 - i:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

print(numbers)
