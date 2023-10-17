def taken_numbers(digit_list):
    take_list = []
    for item in range(len(digit_list)):
        if item % 2 == 0:
            take_list.append(int(digit_list[item]))
    return take_list


def skipped_numbers(digit_list):
    skip_list = []
    for item in range(len(digit_list)):
        if item % 2 != 0:
            skip_list.append(int(digit_list[item]))
    return skip_list


def hidden_message(letter_list,take_list, skip_list):
    taken_string = []
    skipped_string = []
    for index in range(len(take_list)):

        if take_list[index] > 0:
            position = int(take_list[index])
            element = ''.join(letter_list[:position])
            taken_string.append(element)
            del letter_list[:position]

        if skip_list[index] > 0:
            position = int(skip_list[index])
            element = ''.join(letter_list[:position])
            skipped_string.append(element)
            del letter_list[:position]
    return ''.join(taken_string)


def main(my_list):

    digit_list = [num for num in my_list if num.isdigit()]
    non_number_list = [letter for letter in my_list if letter not in digit_list]
    taken_element = taken_numbers(digit_list)
    skipped_element = skipped_numbers(digit_list)
    message = hidden_message(non_number_list, taken_element, skipped_element)
    return message


user_input =[char for char in input()]
print(main(user_input))