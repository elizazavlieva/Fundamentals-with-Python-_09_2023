target_values = [int(num) for num in input().split()]
while True:
    user_input = input().split()
    command = user_input[0]
    index = 0
    value = 0
    if command == 'End':
        print('|'.join(str(i) for i in target_values))
        break

    if command == 'Shoot':
        index = int(user_input[1])
        value = int(user_input[2])
        if 0 <= index < len(target_values):
            target_values[index] -= value
            if target_values[index] <= 0:
                target_values.pop(index)

    elif command == 'Add':
        index = int(user_input[1])
        value = int(user_input[2])
        if 0 <= index < len(target_values):
            target_values.insert(index, value)
        else:
            print('Invalid placement!')

    elif command == 'Strike':
        index = int(user_input[1])
        radius = int(user_input[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(target_values):
            del target_values[start:end + 1]
        else:
            print('Strike missed!')
