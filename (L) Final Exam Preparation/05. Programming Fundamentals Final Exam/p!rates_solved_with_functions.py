def plunder(cities, city, population, wealth):
    cities[city][0] -= population
    cities[city][1] -= wealth
    print(f'{city} plundered! {wealth} gold stolen, {population} citizens killed.')
    if cities[city][0] <= 0 or cities[city][1] <= 0:
        cities.pop(city)
        print(f'{city} has been wiped off the map!')
    return cities


def prosper(cities, city, wealth):
    if wealth <= 0:
        print(f'Gold added cannot be a negative number!')
    else:
        cities[city][1] += wealth
        print(f'{wealth} gold added to the city treasury. {city} now has {cities[city][1]} gold.')
    return cities


cities_info = {}
while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    if command[0] in cities_info:
        cities_info[command[0]][0] += int(command[1])
        cities_info[command[0]][1] += int(command[2])
    else:
        cities_info[command[0]] = [int(command[1]), int(command[2])]


while True:
    line = input().split('=>')
    if line[0] == 'End':
        break
    if line[0] == 'Plunder':
        town, people, gold = line[1], int(line[2]), int(line[3])
        cities_info = plunder(cities_info, town, people, gold)
    elif line[0] == 'Prosper':
        town, gold = line[1], int(line[2])
        cities_info = prosper(cities_info, town, gold)

if len(cities_info):
    print(f'Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:')
    for key, value in cities_info.items():
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
