neighborhood_list = list(map(int, input().split('@')))
last_house = 0
jumps_count = 0
while True:
    user_input = input()
    if user_input == 'Love!':
        break
    command = user_input.split(' ')
    if command[0] == 'Jump':
        index = int(command[1])
        jumps_count += 1
        if jumps_count > 1:
            index += last_house
        if index >= len(neighborhood_list):
            jumps_count = 0
            index = 0
        last_house = index
        if neighborhood_list[index] == 0:
            print(f'Place {index} already had Valentine\'s day.')
            continue
        else:
            neighborhood_list[index] -= 2
            if neighborhood_list[index] == 0:
                print(f'Place {index} has Valentine\'s day.')
failed_house = 0
print(f'Cupid\'s last position was {index}.')
for i in neighborhood_list:
    if i > 0:
        failed_house += 1

if failed_house == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {failed_house} places.')