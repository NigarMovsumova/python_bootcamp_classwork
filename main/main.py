# from core.app import print_numbers_desc


# ascending
def print_numbers_asc(num1, num2):
    for i in range(num1, num2):
        print(i, end=',  ')


# print_numbers_desc(10, 0)

if __name__ == '__main__':
    print_numbers_asc(1, 11)
