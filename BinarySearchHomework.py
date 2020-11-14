# 1. Binary search vasitəsilə verilən ədədin list-də ilk və son indeksini tapmaq gərəkir.
# Əgər nömrə listdə yoxdursa, və ya 1 dəfə rast gəlinirsə, bunuda qeyd etməyiniz gərəkir.

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

index_list = []

while left <= right:
    if target > numbers[middle]:
        left = middle + 1
    else:
        right = middle - 1
    middle = (left + right) // 2
    if numbers[middle] == target:
        index_list.append(middle)
        print(index_list)
        left = middle
        right = len(numbers) -1

print(index_list)

if left > right:
    print('Number is not found')
else:
    print(middle)


# from random import randint
#
#
# def create_randomized_list():
#     numbers = []
#     for i in range(0, 10):
#         numbers.append(randint(0, 5))
#     return numbers
#
#
# def find_number_index(numbers, target):
#     index_list = []
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             index_list.append(i)
#     print(index_list[0], '  ', index_list[-1])
#
#
# def find_number(numbers, target):
#     for i in range(0, len(numbers)):
#         if numbers[i] == target:
#             return i
#     return -1
#
#
# numbers = create_randomized_list()
# print(numbers)
# # print(find_number(numbers, 5))
# find_number_index(numbers, 0)
