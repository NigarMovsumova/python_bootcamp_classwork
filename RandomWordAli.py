import random as i

letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "q", "e", "r", "t"]
list = i.choices(letters, weights=None, k=20)
generated_word = ''
for i in range(0, len(list)):
    generated_word += list[i]
print(list)
print(generated_word)
