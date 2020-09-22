# for letter in 'Africa':
#    print(letter)

# print(letter)

# range - 0 - 9 [0, 1, 2, 3, 4]
# number = range(0, 5)
# print(number)

# for number in range(26, -3, -4):
#    print(number)
# 0-14 - ushaqliq
# 15 - 18 - yeniyetme
# 18 - 35 - genclik
# 35 - 50 - orta yash
# 50 -70 - size kredit verilmir
# 70 - 101 - ezrailin qenimi

# for age in range(0, 101):
#    if age <= 50:
#        print(age, 'is young age')
#    elif age > 50:
#        print(age, 'is wise age')

# for age in range(0, 101):
#    if age <= 14:
#        print(age, 'Childhood')
#    elif age <= 18:
#        print('Teenager')
#    elif age <= 35:
#        print('Youth')
#    elif age <= 50:
#        print('Middle')
#    elif age <= 70:
#        print('No debt for you')
# #    else:
#         print('Game over')


# 3) İstifadəçi 1-20 arası ədəd daxil edir. Ədəd sadədirsə True , mürəkkəbdirsə False çap olunsun.
# (Sadə ədədlər yalnız özünə və 1-ə bölünən ədədlərdir)

isPrime = True
number = int(input('Enter the number: '))
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

print(isPrime)

# 5) Maximum 4 rəqəmli ədəd daxil edilir. Ədədin neçə rəqəmdən ibarət olduğunu
# hesablayan program yazın.
