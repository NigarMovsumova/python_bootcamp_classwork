# İstifadəçi manqo, avokado, kivi alır
# və hərəsindən neçə kilo aldığını qeyd edir.
# Manqo kilosunun qiymeti - 1.5 azn
# Avokado - 8 azn.
# kivi - 2 azn.
# İstifadəçi bazarlığa nə qədər pul
# xərcləyəciyini qeyd edin.

mango_weight = float(input('Enter mango weight: '))
avocado_weight = float(input('Enter avocado weight: '))
kiwi_weight = float(input('Enter kiwi weight: '))
money_amount = float(input('Enter money amount you have: '))
price = mango_weight * 1.5 + avocado_weight * 8 + kiwi_weight * 2
print(money_amount >= price)
print(money_amount - price)
print(mango_weight + kiwi_weight + avocado_weight)

# discount_percentage % endirim
# price -  ilkin qiymet
#
# price - price * discount_percentage /100

# price_after_10_percent_discount

