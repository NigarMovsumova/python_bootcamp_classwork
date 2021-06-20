def sum_numbers(*args):
    numbers_sum = 0
    for i in args:
        numbers_sum += i
    return numbers_sum


# print(sum_numbers(0, 1, 2, 3, 4, 5, 6.7))

# print('sdhsgd', 'sdhgsd', sep=' * ', end='.')


def print_user_info(*args, name, surname, patronymic):
    print(name, surname, patronymic)


print_user_info(1, patronymic='Akif', surname='Movsumova', name='Nigar')
