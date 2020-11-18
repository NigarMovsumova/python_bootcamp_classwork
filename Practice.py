raw_strings = [r"test\nhello\t", r'y\\', r'1234']


# funksiyaya set gonderilir
# o setde raw stringler var
# raw stringlerde \ simvolunu silib
# uzunlugu cut olanlari bir sete,
# uzunlugu tek olanlari diger sete ayirmaq gerekir (nested funksiya istifade edin bunun uchun)

def modify_set(raw_strings):
    for i in range(len(raw_strings)):
        raw_strings[i] = raw_strings[i].replace("\\", '')

    def separate_strings():
        odd_length_strings = set()
        even_length_strings = set()
        for i in raw_strings:
            if len(i) % 2 == 0:
                even_length_strings.add(i)
            else:
                odd_length_strings.add(i)
        print('even:{}'.format(even_length_strings))
        print('odd:{}'.format(odd_length_strings))

    separate_strings()


modify_set(raw_strings)
