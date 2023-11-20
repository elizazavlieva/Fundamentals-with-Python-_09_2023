import re

name_pattern = r'\%([A-Z][a-z]+[^\|\$\.\%])\%'
product_pattern = r'\<(\w+[^\|\$\.\%])\>'
count_pattern = r'\|([0-9]+[^\|\$\.\%]*)\|'
price_pattern = r'([1-9]+[\.0-9]*)\$'
total_income = 0

while True:
    total_product_price = 0
    command = input()
    if command == 'end of shift':
        break
    name = re.findall(name_pattern, command)
    product = re.findall(product_pattern, command)
    count = re.findall(count_pattern, command)
    price = re.findall(price_pattern, command)
    if len(name) != 0 and len(product) != 0 \
            and len(count) != 0 and len(price) != 0:
        total_product_price = int(count[0]) * float(price[0])
        total_income += total_product_price
        print(f"{''.join(name)}: {''.join(product)} - {total_product_price:.2f}")

print(f"Total income: {total_income:.2f}")
