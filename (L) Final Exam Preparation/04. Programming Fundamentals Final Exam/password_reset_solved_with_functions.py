def take_odd(some_string):
    new_password = ''
    for position, value in enumerate(some_string):
        if position % 2 != 0:
            new_password += value
    print(new_password)
    return new_password


def cut(some_string, start_index, str_length):
    end_index = start_index + str_length
    some_string = some_string[:start_index] + some_string[end_index:]
    print(some_string)
    return some_string


def substitute(some_string, substr, replacement):
    if substr in some_string:
        some_string = some_string.replace(substr, replacement)
        print(some_string)
    else:
        print('Nothing to replace!')
    return some_string


password = input()

command = input().split()
while command[0] != 'Done':
    if command[0] == 'TakeOdd':
        password = take_odd(password)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        password = cut(password, index, length)
    elif command[0] == 'Substitute':
        substring, replace = command[1], command[2]
        password = substitute(password, substring, replace)
    command = input().split()

print(f'Your password is: {password}')
