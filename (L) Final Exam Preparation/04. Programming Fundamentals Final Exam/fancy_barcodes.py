import re

product_pattern = r'([@][#]+)([A-Z]([A-Za-z0-9]{4,})[A-Z])([@][#]+)'
digit_pattern = r'\d+'

n = int(input())

for item in range(n):
    command = input()
    product = re.findall(product_pattern, command)
    if product:
        product_group = '00'
        digit = re.findall(digit_pattern, product[0][1])
        if digit:
            product_group = ''.join(digit)
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
