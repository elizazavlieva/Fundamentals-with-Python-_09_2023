def sum_of_even_end_odd_num(num):
    even_sum = 0
    odd_sum = 0
    for i, item in enumerate(num):
        index = int(item)
        if index % 2 == 0:
            even_sum += index
        else:
            odd_sum += index
    return f' Odd sum = {odd_sum}, Even sum = {even_sum}'


number = input()
print(sum_of_even_end_odd_num(number))