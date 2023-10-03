pirate_ship_status = [int(num) for num in input().split('>')]
warship_status = [int(num) for num in input().split('>')]
max_health = int(input())
victory = False
loss = False
while True:
    command = input().split()
    if command[0] == 'Retire' or victory or loss:
        break
    elif command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                victory = True

    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if (0 <= start_index < len(pirate_ship_status)) and 0 <= end_index < len(pirate_ship_status):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    loss = True
                    break

    elif command[0] == 'Repair':
        repair_index = int(command[1])
        health = int(command[2])
        if 0 <= repair_index < len(pirate_ship_status):
            pirate_ship_status[repair_index] += health
            if pirate_ship_status[repair_index] > max_health:
                pirate_ship_status[repair_index] = max_health

    elif command[0] == 'Status':
        count = 0
        for position, item in enumerate(pirate_ship_status):
            health_status = item / max_health
            if health_status < 0.20:
                count += 1
        print(f'{count} sections need repair.')
if victory:
    print('You won! The enemy ship has sunken.')
elif loss:
    print(f'You lost! The pirate ship has sunken.')
else:
    pirate_ship_sum = sum(i for i in pirate_ship_status)
    warship_sum = sum(j for j in warship_status)
    print(f'Pirate ship status: {pirate_ship_sum}')
    print(f'Warship status: {warship_sum}')