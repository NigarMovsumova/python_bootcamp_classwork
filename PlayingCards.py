# 5. İstiadəçi 0-dan 35-ə kimi ədəd daxil edir .
# 36-ədədlik oyun kartlarına uyğun olaraq, bu
# ədədə uyğun işarəni (ürək, xaç,pika, kərpic) və onun dəyərini (
# 6,7,8,9,10,valet,dama,karol,tuz) qaytaran program yazın. (36 if və ya 36 switch lazım
# deyil) . Başqa yollarla yazmağı yoxlayın . ( ardıcıllıq , ÜRƏK,PİKA,KƏRPİC,XAÇ.
# Məsələn 11 yazılsa, ekrana 8 pika yazısı çıxmalıdır, 0 daxil olunarsa - 6Ürək və s.)

# +6
# 0 - 6Hearts
# 1 - 7Hearts
# 2 - 8Hearts
# 3 - 9Hearts
# 4 - 10Hearts
# 5 - ValetHearts = 11
# 6 - DamaHearts = 12
# 7 - KorolHearts = 13
# 8 - TuzHearts = 14
#
# -3
# 9 - 6
# 10 - 7
# 11 - 8
# 12 - 9
# 13 - 10
# 14 - Valet
# 15 - Dama
# 16 - Korol
# 17 - Tuz
#
# -12
# 18 - 6
# 19 - 7
# 20 - 8
# 21 - 9
# 22 - 10
# 23 - Valet
# 24 - Dama
# 25 - Korol
# 26 - Tuz
#
# -21
# 27 - 6
# 28 - 7
# 29 - 8
# 30 - 9
# 31 - 10
# 32 - Valet
# 33 - Dama
# 34 - Korol
# 35 - Tuz
#
# 0- 8 - Hearts
# 9 - 17 - Pikes
# 18 - 26 - Tiles
# 27 - 35 - Clovers

valet = 11
dama = 12
korol = 13
tuz = 14

card_id = int(input('Enter the card\'s id: '))

for i in range(6, -22, -9):
    if (card_id + i) % 11 == 0:
        print('Valet')
        break
    elif (card_id + i) % 12 == 0:
        print('Dama')
        break
    elif (card_id + i) % 13 == 0:
        print('Korol')
        break
    elif (card_id + i) % 14 == 0:
        print('Tuz')
        break
    else:
        print(card_id + i)
        break

if card_id in range(0, 9):
    print('Hearts')
elif card_id in range(9, 18):
    print('Pikes')
elif card_id in range(18, 27):
    print('Tiles')
elif card_id in range(27, 36):
    print('Clovers')
else:
    print('Incorrect id')
