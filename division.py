# 1-1000 araliq verilir.
# Hemin araliqda eyni zamanda 3, 5 ve 7e
# tam bolunen ededleri tapin ve chap edin.

# 105 / 3 = 35
# 105 / 5 = 21
# 105 / 7 = 15
# 105 / 15 = 7
# 105 / 21 = 5
# 105 / 35 = 3

# for i in range(1, 1000):
#     if i % 105 == 0:
#         print(i)

# 1-100 araliq. 2, 3, 5, 7ye ayriliqda bolunen
# ededlerin cemini hesablamaq gerekir.

# numbers_sum = 0
# for i in range(1, 100):
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
#         numbers_sum = numbers_sum + i
# print(numbers_sum)

for i in range(1, 100):
    if i > 98:
        break
    print(i)

# 1. 1-den 100e kimi ededler var, onlarin cemini
# tapmaq lazimdir, cemi 100den ashagi olana kimi.
# 2. 1den 100e kimi 2ye bolunenlerin sayini tapmaq gerekir
# 3. Istifadechi ashagi ve yuxari heddleri daxil edir.
# Hemin intervalda 3e tam bolunen ededlerin hasilini tapin.
# 4. Istifadechi ashagi ve yuxari heddleri daxil edir.
# Bu intervalda kvadrati 125den ashagi olanlari
# tapib cemleyin.

# 3 - 15
#
# 3 - 9
# 4 - 16
# ...
# 12 - 144

# 5. 4 reqemli ededin reqemlerini chap edin for vasitesile.
# 6. Istifadechi 1-20 arasi eded daxil edir.
# Eger eded sadedirse True,
# murekkebdirse False chap edin.