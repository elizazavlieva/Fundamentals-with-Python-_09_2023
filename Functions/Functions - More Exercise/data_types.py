def data_type(command, num):
    if command == 'int':
        return f'{int(num) * 2}'
    elif command == 'real':
        return f'{(float(num) * 1.5):.2f}'
    elif command == 'string':
        return f'${num}$'


user_input = input()
number = input()
print(data_type(user_input, number))
