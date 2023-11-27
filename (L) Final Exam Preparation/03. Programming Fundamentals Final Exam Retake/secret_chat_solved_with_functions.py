def insert_space(line, position):
    line = line[:position] + ' ' + line[position:]
    print(line)
    return line


def reverse(line, some_string):
    if some_string in line:
        reversed_string = some_string[::-1]
        line = (line.replace(some_string, '')) + reversed_string
        print(line)
    else:
        print('error')
    return line


def change_all(line, some_string, replacement_string):
    line = line.replace(some_string, replacement_string)
    print(line)
    return line


message = input()

while True:
    command = input().split(':|:')
    if command[0] == 'Reveal':
        break
    elif command[0] == 'InsertSpace':
        index = int(command[1])
        message = insert_space(message, index)
    elif command[0] == 'Reverse':
        substring = command[1]
        message = reverse(message, substring)
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        message = change_all(message, substring, replacement)

print(f'You have a new text message: {message}')
