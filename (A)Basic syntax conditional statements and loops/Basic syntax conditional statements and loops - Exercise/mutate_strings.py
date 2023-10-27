first_word = input()
second_word = input()
last_printed_word = first_word
for i in range(len(first_word)):
    left_part = second_word[:i+1]
    right_part = first_word[i+1:]
    new_string = left_part + right_part
    if last_printed_word == new_string:
        continue
    else:
        print(new_string)
        last_printed_word = new_string
