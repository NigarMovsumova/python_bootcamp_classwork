# 2 funksiya var, biri verilen setrin uzunlugunu,
# digeri ise sadece setrin ozunu print edir


def get_string_length(string):
    return len(string)


def print_string(string):
    print(string)


def pass_string(string_function):
    return string_function('Ted')



print(pass_string(get_string_length))
pass_string(print_string)
