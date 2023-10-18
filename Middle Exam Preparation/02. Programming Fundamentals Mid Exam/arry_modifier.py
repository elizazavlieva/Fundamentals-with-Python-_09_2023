def modify_elements(value):

    while True:
        user_input = input().split()
        command = user_input[0]
        if len(user_input) > 1:
            index_one = int(user_input[1])
            index_two = int(user_input[2])
        if command == 'end':
            break
        elif command == 'swap':
            value[index_one], value[index_two] = value[index_two], value[index_one]
        elif command == 'multiply':
            value[index_one] = value[index_one] * value[index_two]
        elif command == 'decrease':
            value = [num - 1 for num in value]
    value = [str(num) for num in value]
    return ', '.join(value)


initial_value = [int(num) for num in input().split()]
print(modify_elements(initial_value))