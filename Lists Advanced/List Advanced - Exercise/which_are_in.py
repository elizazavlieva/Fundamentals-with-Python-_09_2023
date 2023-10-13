
first_sequence = input().split(', ')
second_sequence = input().split(', ')
substring_list = []
for first in first_sequence:
    for second in second_sequence:
        if first in second:
            substring_list.append(first)
            break

print(substring_list)