# 1. Istifadeci vezifesini daxil edir.
# 2. Hemin vezifeye esasen, texmini maash ortalamasi qaytarilir.
# 3. Fehle - 400 - 800 AZN
# 4. Usta - 800 - 1500 AZN
# 5. Programmer - 700 - 7000 AZN
# 6. Product Manager - 2000 - 6000 AZN
# 7. Call Center Emekdashi - 400 - 1600 AZN
# 8. Logistika Mutexessisi - 800 - 7000 AZN
# Funksiya vasitesile bu mentiqi yazmaq gerekir,
# Maash araligi qaytarmalidir funksiya ve bashqa
# moduldan qaytarilmalidir.

# def check_salary_by_position(position_id):
#     salaries = ['Laborer - 400-800 AZN',
#                 'Master - 800-1500 AZN',
#                 'Programmer - 700-7000 AZN',
#                 'Product Manager - 2000-6000 AZN',
#                 'Call Center Agent - 400-1600 AZN',
#                 'Logistics Specialist - 800 - 7000 AZN']
#
#     if 0 <= position_id < len(salaries):
#         return salaries[position_id]
#     return "This position is not in the list"
#
# position_id = int(input('''
# Available positions:
# 0. Laborer
# 1. Master
# 2. Programmer
# 3. Product Manager
# 4. Call Center Agent
# 5. Logistics Specialist
# Please choose your position: '''))
# salary_range = check_salary_by_position(position_id)
# print(salary_range)


def check_salary_by_position(position_id):
    positions = ['Laborer', 'Master', 'Programmer',
                 'Product Manager', 'Call Center Agent',
                 'Logistics Specialist']
    AZN = ' AZN'
    salaries = ['400-800',
                '800-1500',
                '700-7000',
                '2000-6000',
                '400-1600',
                '800 - 7000']

    if 1 <= position_id <= len(salaries):
        return positions[position_id - 1] + \
               ' ' + salaries[position_id - 1] + AZN
    return "This position is not in the list"


print('Welcome to the SalaryApp.')
user_input = ''
while user_input != 'x':
    position_id = int(input('''
    Available positions:
    1. Laborer
    2. Master 
    3. Programmer
    4. Product Manager 
    5. Call Center Agent
    6. Logistics Specialist
    Please choose your position: '''))
    salary_range = check_salary_by_position(position_id)
    print(salary_range)
    user_input = input('If you want to close the app, enter x: ')

print('Have a good day !')
