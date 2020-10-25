

#def divided_by_9(n):
#    for i in range(1, n):
#        if i % 9 == 0:
#            # sum += i


#print(sum)

def divided_by_9_with_recursion(n):
    # print(n)
    if n <= 1:
        return 0
    elif n % 9 == 0:
        return n + divided_by_9_with_recursion(n - 9)


print(divided_by_9_with_recursion(27))
