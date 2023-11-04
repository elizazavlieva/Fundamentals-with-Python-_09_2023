
phonebook = {}
n = 0
while True:
    command = input().split('-')
    if len(command) < 2:
        n = int(command[0])
        break
    name = command[0]
    number = command[1]
    if name not in phonebook:
        phonebook[name] = number

for i in range(n):
    name = input()
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')
