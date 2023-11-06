n = int(input())
parking_info = {}

for car in range(n):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate = command[2]
        if username in parking_info:
            print(f'ERROR: already registered '
                  f'with plate number {license_plate}')
        else:
            parking_info[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_info:
            print(f'ERROR: user {username} not found')
        else:
            parking_info.pop(username)
            print(f'{username} unregistered successfully')

for k, v in parking_info.items():
    print(f'{k} => {v}')
