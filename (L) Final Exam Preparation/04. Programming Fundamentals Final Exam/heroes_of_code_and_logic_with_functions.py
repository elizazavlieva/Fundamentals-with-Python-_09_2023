def cast_spell(heroes, name, mp_needed, spell):
    if heroes[name][1] >= mp_needed:
        heroes[name][1] -= mp_needed
        print(f'{name} has successfully cast '
              f'{spell} and now has {heroes[name][1]} MP!')
    else:
        print(f'{name} does not have enough MP to cast {spell}!')
    return heroes


def take_damage(heroes, name, dmg, attacker):
    heroes[name][0] -= dmg
    if heroes[name][0] > 0:
        print(f'{name} was hit for {dmg} HP by '
              f'{attacker} and now has {heroes[name][0]} HP left!')
    else:
        heroes.pop(name)
        print(f'{name} has been killed by {attacker}!')
    return heroes


def recharge(heroes, name, mana):
    max_mana = 200
    current_mana = heroes[name][1]
    heroes[name][1] += mana
    if heroes[name][1] > max_mana:
        diff = max_mana - current_mana
        heroes[name][1] = max_mana
        print(f'{name} recharged for {diff} MP!')
    else:
        print(f'{name} recharged for {mana} MP!')
    return heroes


def heal(heroes, name, hp_amount):
    max_hp = 100
    current_hp = heroes[name][0]
    heroes[name][0] += hp_amount
    if heroes[name][0] > max_hp:
        diff = max_hp - current_hp
        heroes[name][0] = max_hp
        print(f'{name} healed for {diff} HP!')
    else:
        print(f'{name} healed for {hp_amount} HP!')
    return heroes


num_of_heroes = int(input())
heroes_info = {}

for row in range(num_of_heroes):
    hero, hit_points, mana_points = input().split()
    heroes_info[hero] = [int(hit_points), int(mana_points)]

command = input().split(' - ')
while command[0] != 'End':
    if command[0] == 'CastSpell':
        hero_name, mana_points, spell_name = command[1], int(command[2]), command[3]
        heroes_info = cast_spell(heroes_info, hero_name, mana_points, spell_name)
    elif command[0] == 'TakeDamage':
        hero_name, damage, attacking_hero = command[1], int(command[2]), command[3]
        heroes_info = take_damage(heroes_info, hero_name, damage, attacking_hero)
    elif command[0] == 'Recharge':
        hero_name, mana_amount = command[1], int(command[2])
        heroes_info = recharge(heroes_info, hero_name, mana_amount)
    elif command[0] == 'Heal':
        hero_name, hit_amount = command[1], int(command[2])
        heroes_info = heal(heroes_info, hero_name, hit_amount)

    command = input().split(' - ')

for key, value in heroes_info.items():
    print(f'{key}\nHP: {value[0]}\nMP: {value[1]}')
