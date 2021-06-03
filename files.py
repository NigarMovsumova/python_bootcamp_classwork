username = input('Enter your username: ')
file = open("users", "r")
line = file.readline()
print(len('    nigarm       '))
print(len('    nigarm       '.strip()))
flag = False
while line:
    if username == line.strip():
        flag = True
        break
    line = file.readline()