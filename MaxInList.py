# list
# listde dublikatlar ola biler
# random olmasin
# static olsun list
# max-umu tapirsiniz ve onun listde
# neche defe tekrarlandigini tapirsiniz.

numbers = [1, 2, 3, 4, 4, 4, 4, -7, 8, 8, 4, 3, 3, 8, 8, 3, 4, 5, 6]


def count_max():
    max = numbers[0]
    max_count = 1
    for i in range(1, len(numbers)):
        if numbers[i] == max:
            max_count += 1
        elif numbers[i] > max:
            max_count = 1
            max = numbers[i]
    return max_count


print(count_max())
