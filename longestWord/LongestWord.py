def find_longest_word():
    longest_word = ''
    words = []
    file = open('longestWordPractise.txt')
    file_content = file.read()
    file.close()
    words = file_content.split()
    print(words)
    longest_word = words[0]
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word

    return longest_word


print(find_longest_word())
