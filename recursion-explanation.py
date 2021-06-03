# def recursive_function(counter):
#     print('Recursive function start with counter :{}'.format(counter))
#     if counter == 4:
#         return
#
#     counter += 1
#     recursive_function(counter)
#     print('Recursive function end at counter {}'.format(counter))

# Stack Overflow error

# counter = 0
# recursive_function(counter)

#
# def count_to_ten(count):
#     if count == 10:
#         return
#     print(count)
#     count += 1
#     count_to_ten(count)
#
#
# count = 0
# count_to_ten(count)

# 10dan 1e kimi reqemler chap edilsin rekursiya vasitesile.

# def count_to_ten(count):
#     if count == -1:
#         return
#     print(count)
#     count -= 1
#     count_to_ten(count)
#
#
# count = 10
# count_to_ten(count)

# Rekursiya vasitesile 10dan 0a kimi butun ededlerin cemini tapmaq.

# numbers_sum = 0
# for i in range(0, 11):
#     numbers_sum += i
#
# print(numbers_sum)

# def sum_numbers(counter, numbers_sum):
#     if counter == 11:
#         print(counter)
#         print(numbers_sum)
#         return
#     numbers_sum += counter
#     counter += 1
#     sum_numbers(counter, numbers_sum)
#
#
# counter = 1
# numbers_sum = 0
# sum_numbers(counter, numbers_sum)
