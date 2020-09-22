lenkeran = 42

# while lenkeran <= 56:
#    print(lenkeran)
#    # lenkeran = lenkeran + 1
#    lenkeran += 1

# 5) Maximum 4 rəqəmli ədəd daxil edilir. Ədədin neçə rəqəmdən ibarət olduğunu
# hesablayan program yazın.

#1500
# count = 1
# number = 150
# count = 2
# number = 15
# count = 3
# number = 1
# count = 4
# number = 0
number = int(input('Enter the number: '))
count = 0
while number != 0:
    count += 1
    number //= 10
print('number of digits = ', count)