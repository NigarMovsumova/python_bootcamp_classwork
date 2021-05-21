def test():
    name = input('Enter your name:')
    print('Hello, ', name)
    return name

    # def fill_numbers_list():
    #     print('fill_numbers_list start')
    #     sample_list = []
    #     for i in range(0, 5):
    #         user_input = int(input('Enter number at index {}: '.format(i)))
    #         sample_list.append(user_input)
    #     print('fill_numbers_list success')
    return sample_list


# def fill_numbers_list():
#     print('fill_numbers_list start')
#     sample_list = []
#     length = 6
#     for i in range(0, length):
#         user_input = int(input('Enter number at index {}: '.format(i)))
#         sample_list.append(user_input)
#     print('fill_numbers_list success')
#     return sample_list

def fill_numbers_list(length):
    print('fill_numbers_list start for length: {}'.format(length))
    sample_list = []
    for i in range(0, length):
        user_input = int(input('Enter number at index {}: '.format(i)))
        sample_list.append(user_input)
    print('fill_numbers_list success for length: {}'.format(length))
    return sample_list


# username = test()
# username = test()
# print(username + ' is logged in. ')

# print('script start')
# length = 3
# sample_list = fill_numbers_list(length)
# print(sample_list)
#
# sample_list = fill_numbers_list(5)
# print(sample_list)
#
# sample_list = fill_numbers_list(10)
# print(sample_list)

# print('start printing')
# for element in sample_list:
#     print(element)
# print('script end')

# 0. Istifadechi hechne daxil etmir.
# 1. Funksiya listi qebul edir arqument kimi
# 2. Qaytarir listin ededi ortalamasini
# 3. Qaytarilan ededi ortalamani chap etmek gerekir.


# def calc_arithmetic_avg(numbers):
#     numbers_sum = 0
#     for number in numbers:
#         numbers_sum += number
#     return numbers_sum/len(numbers)
#
#
# numbers = [2, 3, 7, 8, 10, 13, 17, 20]
# arithmetic_avg = calc_arithmetic_avg(numbers)
# print(arithmetic_avg)

# İstifadəçi funksiya vasitəsilə yoxlayır ki, daxil etdiyi
# rəqəm positivdir ya neqativ

# def check_if_positive(number):
#     if number >= 0:
#         return True
#     else:
#         return False

# def check_if_positive(number):
#     if number >= 0:
#         return True
#     return False

def check_if_positive(number):
    if number >= 0:
        return True
    return False

print(check_if_positive(5))
print(check_if_positive(10))
print(check_if_positive(-3))
print(check_if_positive(0))