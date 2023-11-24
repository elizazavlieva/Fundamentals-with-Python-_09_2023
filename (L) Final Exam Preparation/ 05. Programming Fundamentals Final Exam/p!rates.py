cities_info = {}
while True:
    line = input().split('||')
    if line[0] == 'Sail':
        break
    else:
        cities, population, gold = line[0], int(line[1]), int(line[2])
        if cities in cities_info:
            cities_info[cities][0] += population
            cities_info[cities][1] += gold
        else:
            cities_info[cities] = [population, gold]

while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    elif command[0] == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        cities_info[town][0] -= people
        cities_info[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities_info[town][0] == 0 or cities_info[town][1] == 0:
            print(f'{town} has been wiped off the map!')
            cities_info.pop(town)

    elif command[0] == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities_info[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities_info[town][1]} gold.')

if len(cities_info):
    print(f'Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:')
    for city, info in cities_info.items():
        print(f'{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
