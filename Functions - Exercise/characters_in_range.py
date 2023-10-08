def characters(first, second):
    char_list = []
    for i in range(ord(first) + 1, ord(second)):
        char_list.append(chr(i))
    return ' '.join(char_list)


first_char = input()
second_char = input()
print(characters(first_char, second_char))
