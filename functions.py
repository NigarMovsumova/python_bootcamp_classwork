import random
import datetime

# 1. Tramvay və ya traleybus biletinin nömrəsi daxil edilir
# (6 rəqəmli), onun Xoşbəxt rəqəm
# olub olmadığını yoxlayın. Xoşbəxt rəqəm - Soldaı
# 3 rəqəmin cəmi sağdakı 3 rəqəmin
# cəminə bərabərdir.
#
# 123321
# 300120

# def is_ticket_happy(ticket_number):
#     # 123321 321 123
#     # print(ticket_number[3:])
#     # print(ticket_number[:3])
#     # print(int(ticket_number[3]) +
#     #       int(ticket_number[4]) +
#     #       int(ticket_number[5]))
#     #
#     # print(int(ticket_number[0]) +
#     #       int(ticket_number[1]) +
#     #       int(ticket_number[2]))
#
#     if int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5]):
#         return True
#     return False

# def is_ticket_happy(ticket_number):
#     left_sum = 0
#     right_sum = 0
#     for i in range(len(ticket_number)):
#         if i < 3:
#             left_sum += int(ticket_number[i])
#         else:
#             right_sum += int(ticket_number[i])
#     return left_sum == right_sum
#
#
# print(is_ticket_happy('123321'))
# print(is_ticket_happy('323456'))

# 1. -30 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan
# massiv yaradın. Birinci müsbət ədqəddən sonra
# gələn bütün rəqəmləri toplayan program yazın.
# [-1, 2, 3, 4]


# def find_sum_brutforce():
#     print(datetime.datetime.now())
#     my_list = []
#     for i in range(0, 1000):
#         my_list.append(random.randint(-30, 20))
#     positive_number_index = None
#     for index in range(0, len(my_list)):
#         if my_list[index] > 0:
#             positive_number_index = index
#             break
#     print(datetime.datetime.now())
#     if positive_number_index is not None:
#         return sum(my_list[positive_number_index + 1:])
#     return 0
#
#
# def find_sum():
#     print(datetime.datetime.now())
#     sample_list = []
#     flag = False
#     numbers_sum = 0
#     for i in range(0, 1000):
#         random_number = random.randint(-30, 20)
#         sample_list.append(random_number)
#         if flag:
#             numbers_sum += random_number
#         if random_number > 0:
#             flag = True
#     print(datetime.datetime.now())
#     return numbers_sum
#
#
# print(find_sum_brutforce())
# print(find_sum())

# 10 ölçülü kəsr ədədlərdən ibarət siyahi yaradın.
# Neçə rəqəmin kəsr hissəsinin olmadığını ekrana çıxaran
# program yazın. (məs: {12, 12.5, 10.1, 1, 2} kəsr hissəsi
# olmayan ədədlər 3)

print(12 % 1)
print(12.2 % 1)
print(15.76 % 1)


def count_int_numbers(numbers_list):
    int_numbers_count = 0
    for number in numbers_list:
        if number % 1 == 0:
            int_numbers_count += 1
    return int_numbers_count


sample_list = [12, 0,  12.5, 17.89, 4.5, 10.1, 1, 2, 6]
print(count_int_numbers(sample_list))