from random import randint


def create_randomized_list():
    numbers = []
    for i in range(0, 10):
        numbers.append(randint(0, 5))
    return numbers


def find_number_index(numbers, target):
    index_list = []
    for i in range(len(numbers)):
        if numbers[i] == target:
            index_list.append(i)
    print(index_list[0], '  ', index_list[-1])


def find_number(numbers, target):
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = create_randomized_list()
print(numbers)
# print(find_number(numbers, 5))
find_number_index(numbers, 0)
