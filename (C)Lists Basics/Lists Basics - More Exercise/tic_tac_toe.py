first_row = input().split(' ')
second_row = input().split(' ')
third_row = input().split(' ')

if first_row[0] == '1' and first_row[1] == '1' and first_row[2] == '1' \
        or second_row[0] == '1' and second_row[1] == '1' and second_row[2] == '1' \
        or third_row[0] == '1' and third_row[1] == '1' and third_row[2] == '1':
    print('First player won')
elif first_row[0] == '2' and first_row[1] == '2' and first_row[2] == '2' or second_row[0] == '2' \
        and second_row[1] == '2' and second_row[2] == '2' or third_row[0] == '2' and third_row[1] == '2' \
        and third_row[2] == '2':
    print('Second player won')
elif first_row[0] == '1' and second_row[0] == '1' and third_row[0] == '1' or first_row[1] == '1' \
        and second_row[1] == '1' and third_row[1] == '1' or first_row[2] == '1' and second_row[2] == '1' \
        and third_row[2] == '1':
    print('First player won')
elif first_row[0] == '2' and second_row[0] == '2' and third_row[0] == '2' or first_row[1] == '2' \
        and second_row[1] == '2' and third_row[1] == '2' or first_row[2] == '2' and second_row[2] == '2' \
        and third_row[2] == '2':
    print('Second player won')
elif first_row[0] == '1' and second_row[1] == '1' and third_row[2] == '1' or \
     first_row[2] == '1' and second_row[1] == '1' and third_row[0] == '1':
    print('First player won')
elif first_row[0] == '2' and second_row[1] == '2' and third_row[2] == '2' or \
     first_row[2] == '2' and second_row[1] == '2' and third_row[0] == '2':
    print('Second player won')
else:
    print("Draw!")