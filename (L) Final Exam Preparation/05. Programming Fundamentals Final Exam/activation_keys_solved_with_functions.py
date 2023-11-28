def contains(key, substr):
    if substr in key:
        print(f'{key} contains {substr}')
    else:
        print('Substring not found!')
    return key


def flip(key, upper_or_lower, start_index, end_index):
    if upper_or_lower == 'Upper':
        key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
    elif upper_or_lower == 'Lower':
        key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]

    print(key)
    return key


def slice_str(key, start_index, end_index):
    key = key[:start_index] + key[end_index:]
    print(key)
    return key


activation_key = input()

command = input().split('>>>')
while command[0] != 'Generate':
    if command[0] == 'Contains':
        substring = command[1]
        activation_key = contains(activation_key, substring)
    elif command[0] == 'Flip':
        kind, start, end = command[1], int(command[2]), int(command[3])
        activation_key = flip(activation_key, kind, start, end)
    elif command[0] == 'Slice':
        start, end = int(command[1]), int(command[2])
        activation_key = slice_str(activation_key, start, end)
    command = input().split('>>>')

print(f'Your activation key is: {activation_key}')
