print("résumé".encode("utf-8"))
print('Üzeyir'.encode('utf-8'))
print("El Niño".encode("utf-8"))
print(b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8'))
print(b'El Ni\xc3\xb1o'.decode("utf-8"))

# b'r\xc3\xa9sum\xc3\xa9'
"El Niño".encode("utf-8")
# b'El Ni\xc3\xb1o'

b"r\xc3\xa9sum\xc3\xa9".decode("utf-8")
# 'résumé'
b"El Ni\xc3\xb1o".decode("utf-8")
# 'El Niño'
