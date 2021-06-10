# def pow_numbers(numbers):
#     # print(numbers)
#     for number in numbers:
#         print('number = ', number, 'yield at: ', number**2)
#         yield number ** 2
#
#
# generator = pow_numbers(range(0, 10))
# for i in generator:
#     print(i)

# for i in (num ** 2 for num in range(0, 10)):
#     print('i=', i)

# 0 - 100, 3 - 101
# generator yaratmaq lazimdir verilen rangeden() yalniz cut reqemlerle

# for i in (num for num in range(3, 100) if num % 2 == 0):
#     print(i)

# for i in range(0, 100, 2)

# generator = pow_numbers(range(1, 100))
# # for gen_num in generator:
# #     print(gen_num)
# #     if gen_num >= 10000:
# #         break
# #
# # for i in (num ** 7 for num in range(0, 100)):
# #     print('i=', i)
# #     if i > 10000:
# #         break
#
# next(generator)
# next(generator)


# print(range(0, 5))
# for i in range(0, 10):
#     print(i)

# 0, 10 **2

# counter = 0
# for i in range(0, 10, counter):
#     print(i)
#     counter += 1

# 1. Decorator yazmaq gerekir.
# Dekoratordan kenar istifadechi reqemi daxil edir
# Dekorator yoxlayir ki, hemin reqem int, floatdir mi.
# eger intdirse, o zaman 2ye vurub, **2 tapsin.
# floatdirsa, kesrnen tam hissesini toplasin.
