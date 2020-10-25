# 1. generate a word +
# 2. generasiya edilmish sozde mutleq vergul, noqte ve nida olmalidir
# 3. o cumleden hemin ishareleri yigishdirib chap edirsiniz.

import string

import RandomWordPractise as random

# list = ['a', 'e', 'i', 'o', 'u', ',', '!', '.']

generated_word = random.generate_any_word(10).rstrip(string.punctuation)
print(generated_word)
word_copy = ''

punctuation = ['?', '!', '.']

for i in range(0, len(generated_word)):
    if generated_word[i] != '?' or generated_word[i] != '!' or generated_word[i] != '.':
        word_copy += generated_word[i]

print(word_copy)
