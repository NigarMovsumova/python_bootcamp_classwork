# İki rəqəm verilir istifadəçi tərəfdən.
# Əgər ilk rəqəm ikincisindən kiçikdirsə, onları artmaya görə,
# Əks halda azalmaya görə çap etmək gərəkir.

# a < b -> a, b
# a > b -> a, b

# İki rəqəm verilir istifadəçi tərəfdən.
# Reqemleri artmaya gore duzun.

# def sort_numbers(first, second, checked):
#     if checked:
#         print(first, second)
#         return
#
#     if first < second:
#         sort_numbers(first, second, True)
#     elif first > second:
#         sort_numbers(first, second, True)
#     else:
#         sort_numbers(first, second, True)


def sort_numbers(first, second, checked):
    if checked:
        print(first, second)
        return
    if first > second:
        sort_numbers(second, first, True)
    else:
        sort_numbers(first, second, True)


sort_numbers(5, 6, False)
sort_numbers(6, 5, False)
sort_numbers(4, 4, False)
