treasure_chest_loot = input().split('|')
command = []
while True:
    command = input().split()
    if command[0] == 'Yohoho!' or len(treasure_chest_loot) <= 0:
        break

    elif command[0] == 'Loot':
        command.pop(0)
        for items in treasure_chest_loot:
            for item in command:
                if item in treasure_chest_loot:
                    continue
                else:
                    treasure_chest_loot.insert(0, item)
    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(treasure_chest_loot):
            pop_element = treasure_chest_loot.pop(index)
            treasure_chest_loot.append(pop_element)

    elif command[0] == 'Steal':
        count = int(command[1])
        stolen_items = []
        if len(treasure_chest_loot) <= count:
            stolen_items = treasure_chest_loot
            treasure_chest_loot = treasure_chest_loot[:- count]
            print(', '.join(stolen_items))


        else:
            stolen_items = treasure_chest_loot[- count:]
            treasure_chest_loot = treasure_chest_loot[:- count]
            print(', '.join(stolen_items))

total = 0
if len(treasure_chest_loot) > 0:
    for item in range(len(treasure_chest_loot)):
        total += len(treasure_chest_loot[item])
    total /= len(treasure_chest_loot)

    print(f'Average treasure gain: {total:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')