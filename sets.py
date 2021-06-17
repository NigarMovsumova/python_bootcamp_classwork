# print(3 == 3.0)
# print(int('3') == 3)
# sample_set = {1, 2, 3.0, 1, 2, 3, '3.', int('3')}
# sample_set = set([1, 2, 3, 4, 1, 1, 1, 2, 3, 4])
# print(sample_set)
# #
# name_set = {'Nigar', 'Tale', 'Mehman'}
# name_set_2 = {'Sugra', 'Aslan', 'Nigar'}
# result_set = name_set.union(name_set_2)
# print(result_set)
#
#
# print(name_set.intersection(name_set_2))
#
# print(name_set)
# print(name_set_2)


sample_set_1 = {1, 2}
sample_set_2 = {1, 3}
sample_set_3 = {3}

# print(1 in sample_set_1)
# print(7 in sample_set_1)

# print(sample_set_2 - sample_set_1)
# print(sample_set_1 - sample_set_2)
# print(sample_set_1.difference(sample_set_2))
#
# print(sample_set_2 | sample_set_1)
# print(sample_set_2.union(sample_set_1))
# print(sample_set_2.union(sample_set_2))
# print(sample_set_3.issubset(sample_set_2))
# print(sample_set_3.issubset(sample_set_1))
# print(sample_set_1.issubset(sample_set_3))

sample_set_1 = {1, 2}
sample_set_2 = {1, 3}
sample_set_3 = {3}
# print(sample_set_2.issuperset(sample_set_3))
# print(sample_set_1.issuperset(sample_set_3))

print(sample_set_2 & sample_set_3)
print(sample_set_2.intersection(sample_set_3))
print(sample_set_1 & sample_set_3)
print(sample_set_1.intersection(sample_set_3))

# Telebelerin siyahisi var. Eger telebe siyahida yoxdursa,
# elave etmek imkani olsun.
# Ve neticede gostersin elave etdi ya artiq var element