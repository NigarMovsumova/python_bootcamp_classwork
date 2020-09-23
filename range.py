# N cütdürsə və 2-5 aralığına daxildirsə, “Qəribə deyil” sözlərini
# çap edin.

n = int(input('Enter the number:'))

# nested condition
if n % 2 == 0:
    if 2 <= n <= 5:
        print('Qeribe deyil')

if n % 2 == 0 and 2 <= n <= 5:
    print('Qeribe deyil')
