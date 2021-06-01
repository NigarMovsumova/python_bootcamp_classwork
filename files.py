username = input('Enter your username: ')
file = open("users", "r")
# file_content = file.read()
# print(type(file_content))
# print(file_content)

line = file.readline()
print(len('    nigarm       '))
print(len('    nigarm       '.strip()))
flag = False
while line:
    if username == line.strip():
        flag = True
        break
    line = file.readline()

file.close()

# print('User exists ? ', flag)

# if flag:
#     print('User exists!')
# else:
#     print('User does not exist!')

if not flag:
    print('User does not exist!')
else:
    print('User exists')

