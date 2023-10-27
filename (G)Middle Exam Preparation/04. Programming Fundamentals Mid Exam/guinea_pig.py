food_qty = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pig_weight = float(input()) * 1000
must_shop = False
for day in range(1, 31):
    food_qty -= 300
    if day % 2 == 0:
        hay -= (food_qty * 0.05)
    if day % 3 == 0:
        cover -= (pig_weight * 1/3)
    if food_qty <= 0 or hay <= 0 or cover <= 0:
        must_shop = True
        break
if must_shop:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {(food_qty / 1000):.2f},'
          f' Hay: {(hay / 1000):.2f}, Cover: {(cover / 1000):.2f}.')