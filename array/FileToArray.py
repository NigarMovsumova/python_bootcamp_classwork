def file_to_array():
    characters = []
    sample_file = open('sample.txt')
    sample_text = sample_file.read()
    sample_file.close()
    for i in sample_text:
        characters.append(i)
    return characters


print(file_to_array())
