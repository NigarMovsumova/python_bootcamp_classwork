sample_file = open('sample_file.txt', 'r+')
file_content = sample_file.read()

sample_file.write('aBrAkAdAbRa')
print(file_content)

file_content = sample_file.read()
print(file_content)


sample_file.close()
print(file_content)


