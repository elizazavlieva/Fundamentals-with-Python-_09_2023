initial_list = input().split('!')

while True:
    user_input = input()
    if user_input == 'Go Shopping!':
        break
    command = user_input.split(' ')
    if command[0] == 'Urgent':
        if command[1] not in initial_list:
            initial_list.insert(0, command[1])
    elif command[0] == 'Unnecessary':
        if command[1] in initial_list:
            initial_list.remove(command[1])
    elif command[0] == 'Correct':
        for index, item in enumerate(initial_list):
            if command[1] == item:
                initial_list[index] = command[2]
                break
    elif command[0] == 'Rearrange':
        if command[1] in initial_list:
            initial_list.remove(command[1])
            initial_list.append(command[1])

print(*initial_list, sep=', ')