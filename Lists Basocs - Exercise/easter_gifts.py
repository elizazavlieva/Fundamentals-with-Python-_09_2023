gift_list = input().split(' ')

while True:
    command = input().split(' ')
    if command[0] == 'No' and command[1] == 'Money':
        break
    if command[0] == 'OutOfStock':
        gift_list = list(map(lambda x: x.replace(command[1], 'None'), gift_list))
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gift_list):
            gift_list[index] = command[1]
    elif command[0] == 'JustInCase':
        gift_list[-1] = command[1]

while 'None' in gift_list:
    gift_list.remove('None')

print(' '.join(gift_list))