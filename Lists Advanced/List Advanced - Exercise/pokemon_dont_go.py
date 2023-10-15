
int_sequence = [int(num) for num in input().split()]
result = 0

while True:
    if len(int_sequence) <= 0:
        print(result)
        break
    index = int(input())
    if 0 <= index < len(int_sequence):
        current_num = int_sequence.pop(index)
    elif index < 0:
        current_num = int_sequence[0]
        new_num = int_sequence[-1]
        int_sequence[0] = new_num
    else:
        current_num = int_sequence[-1]
        new_num = int_sequence[0]
        int_sequence[-1] = new_num
    result += current_num
    for i in range(len(int_sequence)):
        if int_sequence[i] <= current_num:
            int_sequence[i] += current_num
        elif int_sequence[i] > current_num:
            int_sequence[i] -= current_num

