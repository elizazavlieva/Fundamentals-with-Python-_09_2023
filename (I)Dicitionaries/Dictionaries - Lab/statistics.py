product = {}
while True:
    user_input = input().split(': ')
    if user_input[0] == 'statistics':
        break
    products = user_input[0]
    qty = int(user_input[1])
    if products in product.keys():
        product[products] = product.get(products) + qty
    else:
        product[products] = qty


print('Products in stock:')
for i in product:
    print(f'- {i}: {product.get(i)}')
print(f'Total Products: {len(product.keys())} \nTotal Quantity: {sum(product.values())}')