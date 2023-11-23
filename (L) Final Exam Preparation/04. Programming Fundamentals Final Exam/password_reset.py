password = input()

while True:
    command = input().split(' ')
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        password = ''.join([char for index, char in enumerate(password) if index % 2 != 0])
        print(password)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        password = password[:index] + password[length + index:]
        print(password)
    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')
print(f'Your password is: {password}')
