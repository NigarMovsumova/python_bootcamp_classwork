# stringin cut indekslerde olan herfleri
# rekursiya vasitesile print etmek gerekir.

def print_characters(string):
    if string == '':
        return ''
    return string[0] + print_characters(string[2:])


print(print_characters('alinigarriadalpaybehlulnazrin'))
