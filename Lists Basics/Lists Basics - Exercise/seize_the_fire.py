user_input = input().split('#')
water = int(input())
total_fire = 0
effort = 0
cells = []


for i in user_input:
    fire = i.split(' = ')
    fire_type = fire[0]
    fire_level = int(fire[1])
    is_valid = False
    if water < fire_level:
        continue
    if 1 <= fire_level <= 50:
        if fire_type == 'Low':
            is_valid = True
    elif fire_level <= 80:
        if fire_type == 'Medium':
            is_valid = True
    elif fire_level <= 125:
        if fire_type == 'High':
            is_valid = True
    if is_valid:
        cells.append(fire_level)
        water -= fire_level
        effort += fire_level * 0.25
        total_fire += fire_level
print('Cells: ')
for i in cells:
    print(f' - {i}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')