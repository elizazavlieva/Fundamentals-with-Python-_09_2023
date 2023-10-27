def smallest_num(first_num, second_num, third_num):
    my_list = [first_num, second_num, third_num]
    my_list.sort()
    return my_list[0]


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(smallest_num(num_one, num_two, num_three))
