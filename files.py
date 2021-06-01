username = input('Enter your username: ')
file = open("users", "r")
# file_content = file.read()
# print(type(file_content))
# print(file_content)

line = file.readline()
print('**************')
# print(len('    nigarm       '))
# print(len('    nigarm       '.strip()))
while line:
    if username == line.strip():
        print('Users exists!!!')
        break
    line = file.readline()

file.close()
