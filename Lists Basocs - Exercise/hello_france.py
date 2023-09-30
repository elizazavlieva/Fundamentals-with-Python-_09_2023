user_input = input().split('|')
budget = float(input())
bought_items = []
total_item_price =0
for i in user_input:
    new_price = 0
    items = i.split('->')
    is_valid = False
    item_type = items[0]
    item_price = float(items[1])
    if item_type == 'Clothes' and item_price <= 50:
        is_valid = True
    elif item_type == 'Shoes' and item_price <= 35:
        is_valid = True
    elif item_type == 'Accessories' and item_price <= 20.5:
        is_valid = True
    if is_valid:
        if budget - item_price < 0:
            break
        budget -= item_price
        new_price = item_price * 1.4
        total_item_price += item_price
        bought_items.append(new_price)
for i in bought_items:
    print(f'{i:.2f}', end=' ')
print()
print( f'Profit: {(sum(bought_items) - total_item_price):.2f}')
if sum(bought_items) + budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')