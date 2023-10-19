def receipt():
    total_price = 0
    without_tax = 0
    tax = 0
    while True:
        command = input()
        if command == 'special':
            total_price = without_tax + tax
            total_price -= total_price * 0.1
            break
        elif command == 'regular':
            total_price = without_tax + tax
            break
        part_price = float(command)
        if part_price < 0:
            print('Invalid price!')
        else:
            tax += part_price * 0.20
            without_tax += part_price

    if total_price > 0:
        return  f'Congratulations you\'ve just bought a new computer!\n' \
            f'Price without taxes: {without_tax:.2f}$\n' \
            f'Taxes: {tax:.2f}$\n'\
            f'-----------\n' \
            f'Total price: {total_price:.2f}$'
    return 'Invalid order!'


print(receipt())