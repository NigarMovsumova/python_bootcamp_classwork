# Ədədin rəqəmlərinin cəmini tapmaq gərəkir(rekursiya)


def sum_digits(num, digits_sum):
    if num == 0:
        return digits_sum
    digits_sum += num % 10
    return sum_digits(num // 10, digits_sum)


print(sum_digits(123456789, 0))
