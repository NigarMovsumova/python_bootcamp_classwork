from random import randint

def create_randomized_list():
    numbers = []
    for i in range(0, 10):
        numbers.append(randint(0, 5))
    return numbers

numbers = create_randomized_list()
print(numbers)
numbers.sort()
print(numbers)
target = int(input('Enter the searched number:'))

middle = len(numbers) // 2
left = 0
right = len(numbers) - 1

while numbers[middle] != target and left <= right:
        if target > numbers[middle]:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2

if left > right:
    print('Number is not found')
else:
    print(middle)
