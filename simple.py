# def test_function():
#     print('test function start')
#     print('test function end')
#
#
# def test_decorator(function):
#     print('test decorator start')
#
#     def inner_function(*args, **kwargs):
#         print('inner function start')
#         result = function(*args, **kwargs)
#         print('inner function end')
#         return result
#     print('test decorator end')
#     return inner_function
#
#
# # test_decorator(test_function)()
# result_function = test_decorator(test_function)
# print('*'*100)
# result_function()

# 1 funksiyaniz var,
# istifadechi sechimini daxil edir.
# dekorator vasitesile yazmaq gerekir.
# choice = 1
# choice = 2
# else: bele sechim yoxdur.

# 1. Icra et
# 2. Icra etme


# def decorator(choice):
#
#     def executed_func():
#         print('Demo Func started and ended')
#
#     def not_executed_func():
#         print('Demo Func is not executed')
#
#     def wrong_choice_func():
#         print('Wrong Choice')
#
#     if choice == 1:
#         return executed_func
#     elif choice == 2:
#         return not_executed_func
#     else:
#         return wrong_choice_func
#
#
# choice = int(input('''Enter your choice:
# 1. Execute
# 2. Do not execute\n'''))
# result_func = decorator(choice)
# print(result_func)
# result_func()
#
# # decorator(choice)()
#
#
#
#
