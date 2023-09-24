output = ''
while True:
    command = input()
    if command == 'End':
        break
    if command == 'SoftUni':
        continue
    for i in command:
        output += i * 2
    print(output)
    output = ''
