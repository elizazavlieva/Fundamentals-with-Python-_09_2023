def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(summary, third_num):
    return summary - third_num


def add_and_subtract(first_num, second_num, third_num):
    returned_result = sum_numbers(first_num, second_num)
    difference = subtract(returned_result, num_three)
    return difference


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(add_and_subtract(num_one, num_two, num_three))
