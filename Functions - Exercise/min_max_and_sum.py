def min_max_and_sum(list_of_num):
    min_num = min(list_of_num)
    max_num = max(list_of_num)
    result = sum(list_of_num)
    return f'The minimum number is {min_num}\n' \
           f'The maximum number is {max_num}\n' \
           f'The sum number is: {result}'


num_sequence = [int(i) for i in input().split()]
print(min_max_and_sum(num_sequence))