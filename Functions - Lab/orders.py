order = input()
qty = int(input())


def order_price(product, quantity):
    total_price = 0
    coffee = 1.50
    water = 1.00
    coke = 1.40
    snacks = 2.00
    if product == 'coffee':
        total_price = coffee * quantity
    elif product == 'water':
        total_price = water * quantity
    elif product == 'coke':
        total_price = coke * quantity
    elif product == 'snacks':
        total_price = snacks * quantity
    return total_price


print(f'{order_price(order, qty):.2f}')
