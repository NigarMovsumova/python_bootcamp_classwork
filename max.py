# Ardıcılıığın maksimumunu tapmaq gərəkir.


def find_max(numbers, max_number, max_number_index):
    if len(numbers) == 0:
        # print(?)
        print(max_number)
        return max_number

    if numbers[0] > max_number:
        max_number = numbers[0]
    find_max(numbers[1:],  max_number, max_number_index)


numbers = [0, 6, 2, 1, 5, 6, 8, 12, 5, 100, 32, 4, 5, -100]
max_number = numbers[0]
# print(numbers[1:])
# print(numbers[0:])
# for i in range(1, len(numbers)):
#     if numbers[i] > max_number:
#         max_number = numbers[i]
# print(max_number)
max_number_index = 0

find_max(numbers, max_number, max_number_index)

# Sertifikatlar

