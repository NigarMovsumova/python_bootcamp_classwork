def sum_numbers(*args, **kwargs):
    print(kwargs)
    numbers_sum = 0
    for i in args:
        numbers_sum += i
    return numbers_sum


print(sum_numbers(1, test='test'))
print(sum_numbers(1, 3, 4, 56, test='sinaq'))

