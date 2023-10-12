user_input = input().split()
list_of_ints = []
for i in user_input:
    num = int(i)
    list_of_ints.append(num)

while True:
    command = input().split()
    if command[0] == 'end':
        break
    even_num = [even for even in list_of_ints if even % 2 == 0]
    odd_num = [odd for odd in list_of_ints if odd % 2 != 0]
    if command[0] == 'exchange':
        step = int(command[1])
        if 0 <= step < len(list_of_ints):
            list_of_ints = list_of_ints[step + 1:] + list_of_ints[:step + 1]
        else:
            print('Invalid index')
    elif command[0] == 'max':
        if command[1] == 'even' and even_num:
            print((len(list_of_ints) - list_of_ints[::-1].index(max(even_num)) - 1))
        elif command[1] == 'odd' and odd_num:
            print((len(list_of_ints) - list_of_ints[::-1].index(max(odd_num)) - 1))
        else:
            print('No matches')
    elif command[0] == 'min':
        if command[1] == 'even' and even_num:
            print((len(list_of_ints) - list_of_ints[::-1].index(min(even_num)) - 1))
        elif command[1] == 'odd' and odd_num:
            print((len(list_of_ints) - list_of_ints[::-1].index(min(odd_num)) - 1))
        else:
            print('No matches')
    elif command[0] == 'first':
        count = int(command[1])
        if 0 < count <= len(list_of_ints):
            if command[2] == 'even':
                print(even_num[0:count])
            else:
                print(odd_num[0:count])
        else:
            print('Invalid count')
    elif command[0] == 'last':
        count = int(command[1])
        if 0 < count <= len(list_of_ints):
            if command[2] == 'even':
                print(even_num[-count:])
            else:
                print(odd_num[-count:])
        else:
            print('Invalid count')
print(list_of_ints)