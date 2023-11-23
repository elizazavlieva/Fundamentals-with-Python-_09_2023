heroes_num = int(input())
heroes_info = {}
for hero in range(heroes_num):
    hero_name, hit_points, mana = input().split(' ')
    heroes_info[hero_name] = [int(hit_points), int(mana)]

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = command[1], int(command[2]), command[3]
        if heroes_info[hero_name][1] >= mp_needed:
            heroes_info[hero_name][1] -= mp_needed
            if heroes_info[hero_name][1] < 0:
                heroes_info[hero_name][1] = 0
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name][1]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        heroes_info[hero_name][0] -= damage
        if heroes_info[hero_name][0] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_info[hero_name][0]} HP left!')
        else:
            heroes_info.pop(hero_name)
            print(f'{hero_name} has been killed by {attacker}!')
    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])
        heroes_info[hero_name][1] += amount
        if heroes_info[hero_name][1] > 200:
            amount = 200 - (heroes_info[hero_name][1] - amount)
            heroes_info[hero_name][1] = 200
        print(f'{hero_name} recharged for {amount} MP!')
    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])
        heroes_info[hero_name][0] += amount
        if heroes_info[hero_name][0] > 100:
            amount = 100 - (heroes_info[hero_name][0] - amount)
            heroes_info[hero_name][0] = 100
        print(f'{hero_name} healed for {amount} HP!')

for key, value in heroes_info.items():
    print(f'{key}\nHP: {value[0]}\nMP: {value[1]}')
