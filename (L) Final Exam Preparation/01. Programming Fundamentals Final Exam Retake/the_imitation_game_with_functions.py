def move(message, num_of_letters):
    n = num_of_letters
    return message[n:] + message[:n]


def insert(message, index, value):
    return message[:index] + value + message[index:]


def change_all(message, substring, replacement):
    return message.replace(substring, replacement)


def solution(message):
    while True:
        command = input().split('|')
        if command[0] == 'Decode':
            print(f'The decrypted message is: {message}')
            break
        elif command[0] == 'Move':
            letters = int(command[1])
            message = move(message, letters)
        elif command[0] == 'Insert':
            position, value = int(command[1]), command[2]
            message = insert(message, position, value)
        elif command[0] == 'ChangeAll':
            substr, replace = command[1], command[2]
            message = change_all(message, substr, replace)


encrypted_message = input()
solution(encrypted_message)
