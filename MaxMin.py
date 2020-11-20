from random import randint


def random_numbers():
    random_numbers = []
    max = -99
    min = 99
    max_index = 0
    min_index = 0
    for i in range(20):
        random_number = randint(0, 20)
        random_numbers.append(random_number)
        if max < random_number:
            max = random_number
            max_index = i
        if min > random_number:
            min = random_number
            min_index = i
    print(random_numbers)
    print('random_numbers[{}] = {}'.format(max_index, max))
    print('random_numbers[{}] = {}'.format(min_index, min))


print(random_numbers())
