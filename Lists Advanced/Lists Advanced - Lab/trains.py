wagons = [0] * int(input())

while True:
    user_input = input().split()
    command = user_input[0]
    people = 0
    index = 0
    if command == 'End':
        print(wagons)
        break
    elif command == 'add':
        people = int(user_input[1])
        wagons[-1] += people

    elif command == 'insert':
        index = int(user_input[1])
        people = int(user_input[2])
        wagons[index] += people

    elif command == 'leave':
        index = int(user_input[1])
        people = int(user_input[2])
        wagons[index] -= people
