test_list = [0, 1, 2, 3]

def list_sum(list):
    if len(list) == 0:
        return 0
    return list[0] + list_sum(list[1:])


print(list_sum(test_list))
