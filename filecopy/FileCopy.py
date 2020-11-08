original_file = open('original.txt', 'r')
copy_file = open('copy.txt', 'r+')

original_file_content = original_file.read()
copy_file.write(original_file_content)

original_file.close()
copy_file.close()