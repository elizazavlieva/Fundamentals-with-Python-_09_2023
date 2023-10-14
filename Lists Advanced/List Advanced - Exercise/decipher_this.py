def secret_message(message):
    new_message = []
    for item in message:
        num = ''
        characters = []
        word = list(item)

        for char in word:
            if char.isdigit():
                num += char
            else:
                characters.append(char)

        characters[0], characters[-1] = characters[-1], characters[0]
        new_word = chr(int(num)) + ''.join(characters)
        new_message.append(new_word)

    return ' '.join(new_message)


user_input = input().split()
print(secret_message(user_input))



