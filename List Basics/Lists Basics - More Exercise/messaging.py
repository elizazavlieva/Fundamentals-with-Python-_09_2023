num_sequence = input().split(' ')
user_input = input()

message_list = []

for sequence in num_sequence:
    current_sum = 0
    for i in sequence:
        current_sum += int(i)

    current_sum %= len(user_input)

    message_list.append(user_input[current_sum])
    user_input = user_input.replace(user_input[current_sum], '', 1)

print(''.join(message_list))