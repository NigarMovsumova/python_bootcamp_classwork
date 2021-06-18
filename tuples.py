# set -> list
# ardicilliq ehemiyyet dashinmir
# dublikatlar yoxdur
# riyazi choxluqlar anlamina gelir
# tuple python

# sample_tuple = tuple(['1', '2'])
# sample_tuple_2 = (1, 2)
# 1. Deyishdirmek olmur
# 2. Siyahiya benzeyir
# 3. Axtarmaq mumkun deyil neyise
# sample_tuple = sample_tuple_2
# print(sample_tuple[0])
# sample_tuple[0] = 6


# print(sample_tuple)
# print(sample_tuple_2)

#
# class TupleItem:
#
#     def __init__(self, i):
#         self.i = i
#
#     def __str__(self):
#         return f'TupleItem: i: {self.i}'


# tuple_item = TupleItem(1)
# tuple_item_2 = TupleItem(2)
#
# object_tuple = (tuple_item, tuple_item_2)
# tuple_item = tuple_item_2
# print(tuple_item)
# tuple_item.i = 3
# print(tuple_item)
# # print(object_tuple)
# print('*'*100)
# for el in object_tuple:
#     print(el)


# number = 1
# int_tuple = tuple([number, 2, 3])
# print(int_tuple)
# number = 4
# print(int_tuple)

# Tupleda olan elementlerin cemini tapmaq.
# int olmalidir

# str tipinden olanlari tapib bir setrde birleshdirin.
sample_tuple = tuple([1, 2, 3, 'n', 4.5, 5, 'i', 'gar', 6])
numbers_sum = 0
for el in sample_tuple:
    if type(el) in [int, float]:
        numbers_sum += el

print(numbers_sum)
