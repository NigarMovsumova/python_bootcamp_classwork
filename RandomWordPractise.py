# 1. funksiya yaradirsiniz
# 2. diger modula import edib icra edirsiniz o funksiyani
# 3. funksiya istenilen herflerden soz yaradib, onu qaytarir.
import random

characters = ['a', 'e', 'i', 'o', 'u', 'r', ',', '!', '.']


def generate_any_word(length=3):
    generated_word = ''
    for i in range(0, length):
        # random_choice = random.choices(range(0, 6), weights=None)
        # generated_word += characters[random_choice[0]]
        random_choice = random.choices(characters, weights=None, k=3)
        generated_word += random_choice[2]
    return generated_word
