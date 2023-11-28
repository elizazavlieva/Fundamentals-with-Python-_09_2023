import re


def valid_barcode(some_string):
    pattern = r'\@[#]+([A-Z][a-zA-Z0-9]{4,}[A-Z])\@[#]+'
    matches = re.findall(pattern, some_string)
    return matches


def digits_in_barcode(some_string):
    pattern = r'\d+'
    matches = re.findall(pattern, some_string)
    if len(matches):
        return ''.join(matches)
    else:
        return '00'


n = int(input())

for line in range(n):
    user_input = input()
    barcode = ''.join(valid_barcode(user_input))
    if len(barcode):
        product_group = digits_in_barcode(barcode)
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
