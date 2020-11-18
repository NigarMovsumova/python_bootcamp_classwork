list1 = [r'test\nhello\t', r'y\\']


def func(list1):
    for i in list1:
        i = i.replace("\\", "")
    print('list1', list1)

    def newfunct():
        evenlist = []
        oddlist = []
        for i in list1:

            if (list1[i]) % 2 == 0:
                list1[i].append(evenlist)
            else:
                list1[i].add(oddlist)
            newfunct()


print(func(list1))
