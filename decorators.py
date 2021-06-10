from time import time


# Positional arguments, Keyword arguments
# Keyword arguments butun positional argumentlerden sonra olmalidir.
# args, kwargs- keyword arguments

# def create_shopping_list(food_name, shopping_lists):
#     shopping_dictionary = {
#         'shah pilaf': ['Rice', 'Lavash', 'Butter', 'Qayisi', 'Shabalid',
#                   'Salt', 'Meat'],
#         'cesar salad': ['Chicken', 'Tuna', 'Kahi', 'Sauce', 'Suxari',
#                    'Salt', 'Olive Oil', 'Tomatoes', 'Cucumber']
#     }
#     try:
#         shopping_lists.append(shopping_dictionary[food_name])
#     except KeyError:
#         shopping_lists.append(["Bizim menyumuza bu yemek yoxdur."])
#
#     return shopping_lists
#
#
# def get_shopping_list(**kwargs):
#     # print(kwargs)
#     # print(kwargs['food_choice'])
#     # print(kwargs['alternative'])
#     shopping_lists = []
#     create_shopping_list(kwargs['food_choice'], shopping_lists)
#     create_shopping_list(kwargs['alternative'], shopping_lists)
#     return shopping_lists
#
#
# def print_list_beautifully(sample_list):
#     for item in sample_list:
#         print(item)
#     print("*" * 100)
#
#
# food_choice = input("What do you want to cook? ")
# alternative = input('Which alternative would you prefer? ')
#
# # shopping_list = get_shopping_list(food_choice, alternative)
# shopping_list = get_shopping_list(alternative=alternative,
#                                   food_choice=food_choice)
# print_list_beautifully(shopping_list)
# shopping_list = get_shopping_list(alternative=alternative,
#                                   food_choice=alternative)
# print_list_beautifully(shopping_list)
# shopping_list = get_shopping_list(alternative=food_choice,
#                                   food_choice=food_choice)
# print_list_beautifully(shopping_list)

# def square_nums(test2, nums=[1, 2], test=""):
#     print('test=', test)
#     print('test2=', test2)
#     print('nums=', nums)
#     start = time()
#     print(start)
#     result = [num ** 2 for num in nums]
#     end = time()
#     print(end)
#     print('Completed in {} milliseconds'.format(end - start))
#     return result
#
# nums = []
# for i in range(0, 100000):
#     nums.append(i)

# square_nums([1, 2, 4, 5])
# square_nums(nums)
# square_nums(test2="test2")
#
#
# def demo(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
#
#
# demo()
#
# demo([1, 2, 3, 4], test='test')
#
#
def demo_func():
    result = 0
    for i in range(0, 100):
        result = i ** 3
    return result


def demo_func_2(*args):
    for i in args:
        print(i)


def check_time(func):
    print(func)
    def inner_func(*args, **kwargs):
        print(args, "  ", kwargs)
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('processed function {} in {}'.format(func, end - start))
        return result

    return inner_func


func = check_time(demo_func)
func_2 = check_time(demo_func_2)

print('func = ', func)
print('func2 = ', func_2)
func()
func_2([1, 2, 3, 4])
#
#
# @check_time
# def demo_func_3():
#     print('test demo func 3')
#
#
# demo_func_3()

# Funksiya kwargs qebul edir.
# hemin kwargsda test keywordu varsa, chap edilsin value
# Yoxdursa, qeyd olunsun ki, o cur value yoxdur.


# def kwargs_func(**kwargs):
#     try:
#         print(kwargs['test'])
#     except KeyError:
#         print('There is not such key')


# def kwargs_func(**kwargs):
#     if 'test' in kwargs.values():
#         print(kwargs['test'])
#     else:
#         print('There is not such key')
#
#
# kwargs_func()
# kwargs_func(test='test1')
