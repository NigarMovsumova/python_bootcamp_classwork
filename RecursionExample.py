# 0 - x


def sum_numbers(number):
    if number == 0:
        return 0
    return number + sum_numbers(number - 1)


# number = 5
# return 5 + sum_numbers(4)
# return 4 + sum_numbers(3)
# return 3 + sum_numbers(2)
# return 2 + sum_numbers(1)
# return 1 + sum_numbers(0)
# return 0

number = int(input('Enter the number: '))
print(sum_numbers(number))
