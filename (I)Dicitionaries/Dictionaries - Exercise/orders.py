items = {}
while True:
    line = input()
    if line == 'buy':
        break
    product, price, qnty = line.split()
    if product not in items:
        items[product] = [float(price), int(qnty)]
    else:
        if items[product][0] != float(price):
            items[product][0] = float(price)
        items[product][1] += int(qnty)

for k,v in items.items():
    result = v[0] * v[1]
    print(f'{k} -> {result:.2f}')
