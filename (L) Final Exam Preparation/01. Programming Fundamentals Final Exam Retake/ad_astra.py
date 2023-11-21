import re

text = input()
pattern = r'([|#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
food_info = [list(items) for items in re.findall(pattern, text)]
for item in food_info:
    for i in item:
        if i == '#' or i =='|':
            item.remove(i)

total_calories = sum([int(cal[-1]) for cal in food_info])
days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for food in food_info:
    print(f'Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}')
