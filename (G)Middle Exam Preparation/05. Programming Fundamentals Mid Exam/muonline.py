user_input= input().split('|')
initial_health = 100
health = initial_health
bitcoins = 0
loss = False

amount = 0
for position, room in enumerate(user_input):
    dungeon_room = room.split(' ')
    command = dungeon_room[0]
    number = int(dungeon_room[1])
    if command == 'potion':
        health += number
        amount = number
        if health > initial_health:
            diff = health - initial_health
            health = initial_health
            amount = number - diff
        print(f'You healed for {amount} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {position + 1}')
            loss = True
            break
    if loss:
        break
if not loss:
    print('You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')