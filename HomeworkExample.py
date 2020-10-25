list = []
inner_list_1 = [1, 2, 3, 4, 5, 10]
inner_list_2 = [4, 5, 6, 7, 8, 9]

list.append(inner_list_1)
list.append(inner_list_2)
print(list)

for i in range(0, len(list)):
    for j in range(0, len(inner_list_1)):
        if j == 5:
            print(list[i][j] - 10)
