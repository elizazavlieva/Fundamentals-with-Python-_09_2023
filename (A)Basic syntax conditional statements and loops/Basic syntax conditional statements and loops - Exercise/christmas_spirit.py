decorations = int(input())
days_till_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

total_spirit = 0
total_expense = 0

for day in range(1, days_till_christmas + 1):
    if day % 11 == 0:
        decorations += 2
    if day % 2 == 0:
        total_spirit += 5
        total_expense += decorations * ornament_set_price
    if day % 3 == 0:
        total_spirit += 13
        total_expense += (tree_skirt_price + tree_garland_price) * decorations
    if day % 5 == 0:
        total_expense += decorations * tree_lights_price
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_expense += tree_lights_price + tree_garland_price + tree_skirt_price
if days_till_christmas % 10 == 0:
    total_spirit -= 30
print(f'Total cost: {total_expense}')
print(f'Total spirit: {total_spirit}')
