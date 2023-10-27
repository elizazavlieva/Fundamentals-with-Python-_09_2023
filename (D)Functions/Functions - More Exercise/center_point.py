import math


def center_point(first_x, first_y, second_x, second_y):
    return math.sqrt(math.pow(second_x - first_x, 2.0) + math.pow(second_y - first_y, 2.0))


x_1, y_1, x_2, y_2 = math.floor(float(input())), math.floor(float(input())), \
    math.floor(float(input())), math.floor(float(input()))

first_distance = center_point(x_1, y_1, 0, 0)
second_distance = center_point(x_2, y_2, 0, 0)

if first_distance <= second_distance:
    print(f'({x_1}, {y_1})')
else:
    print(f'({x_2}, {y_2})')
