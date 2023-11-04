
counter = 0
resource = {}
current_command = ''

while True:
    command = input()
    if command == 'stop':
        break
    if counter % 2 == 0:
        if command not in resource:
            resource[command] = 0
        current_command = command

    else:
        resource[current_command] += int(command)
    counter += 1

for k, v in resource.items():
    print(f'{k} -> {v}')
