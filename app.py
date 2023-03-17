# import test
# import random

# print(__name__)
# # print(t.__name__)
#
# print(random.__name__)
# print(test.__name__)
# name = input('Enter your name: ')


# 2 funksiya var, biri 10dan 1e kimi chap edir reqemleri, digeri ise
# 1den 10a kimi chap edir. heresi ferqli moduldadir
# 10dan 1e kimi chap eden funksiyani diger modulda chagirmaq gerekir.
# 1den 10a kimi chap eden funksiyani diger modulda chagirmaq gerekir.
# if __name__ = '__main__' - test etmek ucun

# from main import print_numbers_asc


# descending
def print_numbers_desc(num1, num2):
    for i in range(num1, num2, -1):
        print(i, end=',  ')


# print_numbers_asc(1, 11)

# if __name__ == '__main__':
#     print_numbers_desc(10, 0)

