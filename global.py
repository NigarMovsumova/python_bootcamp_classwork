
global_var = 'global'
x = 'global'
name = 'Nigar'

# def test():
#     global_var = 'test'
#     local_var = 'local'
#     print(local_var)
#     print(global_var)


def test():
    global global_var
    # global name
    global_var = 'test'
    # print(name)
    print(global_var)
    # name = 'Yusif'
    # print(name)


# def outer():
#     x = "local"
#
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)


# outer()

test()
print(global_var)

# print('global: ', x)