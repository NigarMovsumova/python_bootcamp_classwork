# a - z
# a b c d e - z
# z y x - a
#
# print(ord('c'))
# print(chr(97))

# print(chr(122))
# print(chr(123))


def print_alphabet(character_index):
    if character_index == 123:
        return
    print(chr(character_index))
    return print_alphabet(character_index + 1)


print_alphabet(97)
