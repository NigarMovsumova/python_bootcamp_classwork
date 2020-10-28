from random import randint

length = 9
numbers = []
for i in range(length):
    numbers.append(randint(1, 99))
print(numbers)

for i in range(int((length - 1) / 2)):
    for j in range(int((length - i - 1) / 2)):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
