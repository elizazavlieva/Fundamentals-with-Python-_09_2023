num_of_cars = int(input())
cars_info = {}

for num in range(num_of_cars):
    car, mileage, fuel = input().split('|')
    cars_info[car] = [int(mileage), int(fuel)]

while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars_info[car][1] < fuel:
            print('Not enough fuel to make that ride')
        else:
            cars_info[car][0] += distance
            cars_info[car][1] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars_info[car][0] >= 100000:
            print(f'Time to sell the {car}!')
            cars_info.pop(car)
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        cars_info[car][1] += fuel
        if cars_info[car][1] > 75:
            diff = 75 - (cars_info[car][1] - fuel)
            cars_info[car][1] = 75
            print(f'{car} refueled with {diff} liters')
        else:
            print(f'{car} refueled with {fuel} liters')
    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        cars_info[car][0] -= kilometers
        if cars_info[car][0] < 10000:
            cars_info[car][0] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')\

for key, value in cars_info.items():
    print(f'{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
