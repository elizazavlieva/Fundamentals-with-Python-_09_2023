def sorted_items(list_of_num):
    sorted_list = []
    for i in list_of_num:
        sorted_list.append(int(i))
    sorted_list.sort()
    return sorted_list


sequence_of_num = input().split()
print(sorted_items(sequence_of_num))
