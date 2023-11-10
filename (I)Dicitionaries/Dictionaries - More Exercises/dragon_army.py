n = int(input())
dragons = {}
for i in range(n):
    command = input().split()
    dragon_type = str(command[0])
    name = str(command[1])
    damage = 45 if command[2] == 'null' else int(command[2])
    health = 250 if command[3] == 'null' else int(command[3])
    armor = 10 if command[4] == 'null' else int(command[4])
    if dragon_type not in dragons:
        dragons[dragon_type] = {name: [damage, health, armor]}
    else:
        dragons[dragon_type][name] = [damage, health, armor]

for category, dragon in dragons.items():
    average_damage = sum([stats[0] for stats in dragon.values()]) / len(dragon)
    average_health = sum([stats[1] for stats in dragon.values()]) / len(dragon)
    average_armor = sum([stats[2] for stats in dragon.values()]) / len(dragon)
    sorted_dragons = dict(sorted(dragons[category].items(), key=lambda x: x[0]))
    print(f'{category}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})')
    for name, statistic in sorted_dragons.items():
        print(f'-{name} -> damage: {statistic[0]}, health: {statistic[1]}, armor: {statistic[2]}')
