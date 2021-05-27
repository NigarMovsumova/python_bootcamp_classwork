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

def is_ticket_happy(ticket_number):
    left_sum = 0
    right_sum = 0
    for i in range(len(ticket_number)):
        if i < 3:
            left_sum += int(ticket_number[i])
        else:
            right_sum += int(ticket_number[i])
    return left_sum == right_sum


print(is_ticket_happy('123321'))
print(is_ticket_happy('323456'))

#
# 1. -30 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan
# massiv yaradın. Birinci müsbət ədəddən sonra
# gələn bütün rəqəmləri toplayan program yazın.

# [-1, 2, 3, 4]


