user_input = input().split(', ')
num_list = []
zero_list = []

for i in user_input:
    num = int(i)
    if num != 0:
        num_list.append(num)
    else:
        zero_list.append(num)
print(num_list + zero_list)