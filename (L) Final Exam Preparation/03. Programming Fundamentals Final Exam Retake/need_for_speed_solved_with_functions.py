def drive(info, car, km_distance, fuel_amount):
    if info[car][1] < fuel_amount:
        print('Not enough fuel to make that ride')
    else:
        info[car][0] += km_distance
        info[car][1] -= fuel_amount
        print(f'{car} driven for {km_distance} kilometers. {fuel_amount} liters of fuel consumed.')
        if info[car][0] >= 100000:
            info.pop(car)
            print(f'Time to sell the {car}!')
    return info


def refuel(info, car, fuel_amount):
    max_fuel = 75
    info[car][1] += fuel_amount
    if info[car][1] > max_fuel:
        diff = max_fuel - (info[car][1] - fuel_amount)
        info[car][1] = max_fuel
        print(f'{car} refueled with {diff} liters')
    else:
        print(f'{car} refueled with {fuel_amount} liters')
    return info


def revert(info, car, km):
    info[car][0] -= km
    if info[car][0] >= 10000:
        print(f'{car} mileage decreased by {km} kilometers')
    else:
        info[car][0] = 10000
    return info


num_of_cars = int(input())
cars_info = {}
for i in range(num_of_cars):
    cars = input().split('|')
    cars_info[cars[0]] = [int(cars[1]), int(cars[2])]

command = input().split(' : ')
while command[0] != 'Stop':
    if command[0] == 'Drive':
        auto, distance, fuel = command[1], int(command[2]), int(command[3])
        cars_info = drive(cars_info, auto, distance, fuel)
    elif command[0] == 'Refuel':
        auto, fuel = command[1], int(command[2])
        cars_info = refuel(cars_info, auto, fuel)
    elif command[0] == 'Revert':
        auto, kilometers = command[1], int(command[2])
        cars_info = revert(cars_info, auto, kilometers)
    command = input().split(' : ')

if len(cars_info):
    for auto_name, stats in cars_info.items():
        print(f'{auto_name} -> Mileage: {stats[0]} kms, Fuel in the tank: {stats[1]} lt.')
