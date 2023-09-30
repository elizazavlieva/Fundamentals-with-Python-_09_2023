working_day_events = input().split('|')
max_energy = 100
coins = 100
single_event = []
current_energy = 100
enough_money = True
for i in working_day_events:
    single_event = i.split('-')
    event = single_event[0]
    value = int(single_event[1])
    if event == 'rest':
        gained_energy = 0
        if current_energy + value > max_energy:
            gained_energy = max_energy - current_energy
            current_energy += gained_energy

        else:
            gained_energy = value
            current_energy += value

        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
    elif event == 'order':
        if current_energy >= 30:
            coins += value
            current_energy -= 30
            print(f'You earned {value} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
            continue
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            print(f'Closed! Cannot afford {event}.')
            enough_money = False
            break
if enough_money:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")