def check_if_car_races(car_name):
    participant_cars = ['Mercedes', 'Red Bull', 'McLaren',
                        'Aston Martin', 'Alpine', 'Ferrari',
                        'AlphaTauri', 'Alfa Romeo', 'Haas',
                        'Williams']
    return car_name in participant_cars

# Listin ichinde Formula-1de ishtirak edecek mashinlari
# tapin.
# def check_if_car_races(car_name):
#     participant_cars = ['Mercedes', 'Red Bull', 'McLaren',
#                         'Aston Martin', 'Alpine', 'Ferrari',
#                         'AlphaTauri', 'Alfa Romeo', 'Haas',
#                         'Williams']
#     for participant_car in participant_cars:
#         if car_name == participant_car:
#             return True
#     return False