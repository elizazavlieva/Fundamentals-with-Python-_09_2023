def merge(line_of_strings, start, end):
    if 0 <= start and end < len(line_of_strings):
        line_of_strings[start:end + 1] = [''.join(line_of_strings[start:end + 1])]
    else:
        if start < 0 and end < len(line_of_strings):
            start = 0
        elif start >= 0 and end >= len(line_of_strings):
            end = len(line_of_strings)
        line_of_strings[start:end + 1] = [''.join(line_of_strings[start:end + 1])]
        return line_of_strings


def divide(line_of_strings, index, partition):
    if len(line_of_strings[index]) < partition:
        step = 1
    else:
        step = len(line_of_strings[index]) // partition
    divide_part = line_of_strings.pop(index)
    start = 0
    for parts in range(partition):
        if parts == partition - 1:
            line_of_strings.insert(index, divide_part[start::])
            break
        else:
            line_of_strings.insert(index, divide_part[start: start + step:])
        start += step
        index += 1
    return line_of_strings


def result(line_of_strings):
    while True:
        user_input = input().split()
        if user_input[0] == '3:1':
            break
        command = user_input[0]
        if command == 'merge':
            beginning = int(user_input[1])
            ending = int(user_input[2])
            merge(line_of_strings, beginning, ending)

        elif command == 'divide':
            position = int(user_input[1])
            slicing = int(user_input[2])
            divide(line_of_strings, position, slicing)
    return ' '.join(line_of_strings)


line = input().split()
print(result(line))
