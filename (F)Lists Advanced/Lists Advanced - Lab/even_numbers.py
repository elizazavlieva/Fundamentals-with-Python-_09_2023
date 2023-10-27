def even_numbers(number):
    index_list = [index for index, num in enumerate(number) if num % 2 == 0]
    return index_list


num_list = [int(num) for num in input().split(', ')]
print(even_numbers(num_list))