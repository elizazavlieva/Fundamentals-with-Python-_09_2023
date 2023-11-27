activation_key = input()

while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        print(f'Your activation key is: {activation_key}')
        break
    elif command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print('Substring not found!')
    elif command[0] == 'Flip':
        style, start_index, end_index = command[1], int(command[2]), int(command[3])
        substring = activation_key[start_index:end_index]
        if style == 'Upper':
            activation_key = activation_key[:start_index] + substring.upper() + activation_key[end_index:]

        elif style == 'Lower':
            activation_key = activation_key[:start_index] + substring.lower() + activation_key[end_index:]
        print(activation_key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        substring = activation_key[start_index:end_index]
        activation_key = activation_key.replace(substring, '')
        print(activation_key)
