from random import randint


def sum_list_elements(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list_elements(numbers[1:])


# [1, 2, 3, 4, 5]
# 1 + 2 + 3 + 4 + 5 + 0 = 15


numbers = []

for i in range(5):
    numbers.append(randint(0, 3))

print(numbers)
print(sum_list_elements(numbers))
