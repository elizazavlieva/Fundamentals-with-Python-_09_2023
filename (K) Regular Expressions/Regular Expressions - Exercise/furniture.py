import re
total_cost = 0
bought_furniture = []
pattern = r'>>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)*)+\!([0-9]+)\b'
while True:
    command = input()
    if command == 'Purchase':
        break
    matches = re.findall(pattern,command)
    if len(matches) != 0:
        for furniture in matches:
            bought_furniture.append(furniture[0])
            total_cost += float(furniture[1]) * int(furniture[3])
print('Bought furniture:')
for items in bought_furniture:
    print(items)

print(f'Total money spend: {total_cost:.2f}')
