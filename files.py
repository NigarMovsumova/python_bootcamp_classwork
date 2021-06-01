# username = input('Enter your username: ')
# file = open("users", "r")
# # file_content = file.read()
# # print(type(file_content))
# # print(file_content)
#
# line = file.readline()
# print(len('    nigarm       '))
# print(len('    nigarm       '.strip()))
# flag = False
# while line:
#     if username == line.strip():
#         flag = True
#         break
#     line = file.readline()
#
# file.close()
#
# # print('User exists ? ', flag)
#
# # if flag:
# #     print('User exists!')
# # else:
# #     print('User does not exist!')
#
# if not flag:
#     print('User does not exist!')
# else:
#     print('User exists')
#
# print('User exists') if flag else print('User does not exist')


with open('users', 'a+') as file:
    # print(file.read())
    file.write('test')
    # print(file.read())

# 1. File yoxdursa, yaradilsin.
# 2. File achilsin, ichi boshdursa, ichine hansisa soz yaziB
# baglamaq lazimdir
# 3. Eger ichi bosh deyilse, o zaman ichinde chap etmek gerekir.




