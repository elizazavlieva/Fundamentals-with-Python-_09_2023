n = int(input())
collection = {}
for line in range(n):
    plants = input().split('<->')
    collection[plants[0]] = [plants[1]]
while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    info = command[1].split(' - ')
    if info[0] in collection.keys():
        if command[0] == 'Rate':
            plant, rating = info[0], info[1]
            collection[plant].append(rating)
        elif command[0] == 'Update':
            plant, new_rarity = info[0], info[1]
            collection[plant][0] = new_rarity
        elif command[0] == 'Reset':
            plant = info[0]
            del collection[plant][1:]
    else:
        print('error')
print('Plants for the exhibition:')
for name, value in collection.items():
    if len(value[1:]) != 0:
        average_rating = (sum([int(num) for num in value[1:]])) / len(value[1:])
    else:
        average_rating = 0
    print(f"- {name}; Rarity: {value[0]}; Rating: {average_rating:.2f}")
