n = int(input())
dragons = {}
for i in range(n):
    command = input().split()
    dragon_type = str(command[0])
    name = str(command[1])
    if command[2] == 'null':
        damage = 45
    else:
        damage = int(command[2])
    if command[3] == 'null':
        health = 250
    else:
        health = int(command[3])
    if command[4] == 'null':
        armor = 10
    else:
        armor = int(command[4])
    if dragon_type not in dragons:
        dragons[dragon_type] = {name: [damage, health, armor]}
    elif name not in dragons[dragon_type]:
        dragons[dragon_type][name] = [damage, health, armor]
    elif name in dragons[dragon_type] and dragon_type in dragons:
        dragons[dragon_type][name] = [damage, health, armor]
for k, v in dragons.items():

    average_damage = 0
    average_health = 0
    average_armor = 0
    sorted_dragons = dict(sorted(v.items(), key=lambda x: x[0]))
    for key, value in sorted_dragons.items():
        for index in range(len(value)):
            if index == 0:
                average_damage += value[index]
            elif index == 1:
                average_health += value[index]
            else:
                average_armor += value[index]
    print(f'{k}::({(average_damage / len(v)):.2f}/{(average_health / len(v)):.2f}/{(average_armor / len(v)):.2f})')
    for key, value in sorted_dragons.items():
        print(f'-{key} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}')
