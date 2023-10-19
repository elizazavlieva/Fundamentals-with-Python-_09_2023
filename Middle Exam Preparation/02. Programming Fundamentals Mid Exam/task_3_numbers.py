def average_value(int_sequence):
    return sum(int_sequence) / len(int_sequence)


def top_five(int_sequence):
    average = (average_value(int_sequence))
    greater_num = []

    for num in int_sequence:
        if average < num:
            greater_num.append(num)
    greater_num.sort(reverse=True)

    if len(greater_num) > 0 and len(greater_num) >= 5:
        return ' '.join([str(num) for index,num in enumerate(greater_num[:5])])
    elif len(greater_num) <= 0:
        return 'No'
    else:
        return ' '.join([str(num) for num in greater_num])


user_input = [int(num) for num in input().split()]
print(top_five(user_input))