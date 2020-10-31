# 100 - 9999 aralığında rəqəmləri fərqli olan bütün tam rəqəmlərin cəmini tapmaq gərəkir.

first_digit = 0
second_digit = 0
third_digit = 0
forth_digit = 0

digits_count = 0
sum = 0

for i in range(102, 9877):
    copy = i
    if i // 1000 == 0:
        third_digit = copy % 10
        copy //= 10
        second_digit = copy % 10
        copy //= 10
        first_digit = copy % 10
        if first_digit != second_digit and first_digit != third_digit and second_digit != third_digit:
            sum += i
    else:
        forth_digit = copy % 10
        copy //= 10
        third_digit = copy % 10
        copy //= 10
        second_digit = copy % 10
        copy //= 10
        first_digit = copy % 10

        if first_digit != second_digit and first_digit != third_digit and first_digit != forth_digit and second_digit != third_digit and second_digit != forth_digit and third_digit != forth_digit:
            sum += i

print(sum)
