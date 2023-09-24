upper_list = ['CODING', 'DOG', 'CAT', 'MOVIE']
lower_list = ['coding', 'dog', 'cat', 'movie']
count = 0
while True:
    command = input()
    if command == 'END':
        break
    if command in upper_list:
        count += 2
    if command in lower_list:
        count += 1
if count > 5:
    print('You need extra sleep')
else:
    print(count)