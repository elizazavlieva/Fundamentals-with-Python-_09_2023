key = [int(num) for num in input().split()]

while True:
    command = input()
    if command == 'find':
        break
    message = ''
    index = 0
    for char in command:
        new_char = chr(ord(char) - key[index])
        message += new_char
        index = (index + 1) % len(key)
    treasure_type = ''
    coordinates = ''
    is_treasure_found = False
    is_coordinates_found = False
    counter = 0
    for char in message:
        if is_treasure_found and char != '&':
            treasure_type += char
        if char == '&':
            is_treasure_found = True
            counter += 1
            if counter == 2:
                is_treasure_found = False
        if is_coordinates_found and char != '>':
            coordinates += char
        if char == '<':
            is_coordinates_found = True

    print(f'Found {treasure_type} at {coordinates}')
