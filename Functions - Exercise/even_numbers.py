def even_numbers(list_of_num):
    even_num = []
    for i in list_of_num:
        if i % 2 == 0:
            even_num.append(i)
    return even_num


number_sequence = [int(num) for num in input().split(' ')]
print(even_numbers(number_sequence))
