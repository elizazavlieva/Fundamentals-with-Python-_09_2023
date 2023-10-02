sequence_of_num = input().split(' ')
left_car_time = 0
right_car_time = 0
middle = len(sequence_of_num) // 2

left_part = list(sequence_of_num[0:middle])
right_part = list(sequence_of_num[middle+1:])
right_part.reverse()

for left_time in left_part:
    if left_time == '0':
        left_car_time *= 0.80
    else:
        left_car_time += int(left_time)
for right_time in right_part:
    if right_time == '0':
        right_car_time *= 0.80
    else:
        right_car_time += int(right_time)

if right_car_time < left_car_time:
    print(f'The winner is right with total time: {right_car_time:.1f}')
else:
    print(f'The winner is left with total time: {left_car_time:.1f}')