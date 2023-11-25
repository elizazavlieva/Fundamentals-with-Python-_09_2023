def rate(plant_info, plant, rating):
    plant_info[plant].append(rating)
    return plant_info


def update(plant_info, plant, new_rarity):
    plant_info[plant][0] = int(new_rarity)
    return plant_info


def reset(plant_info, plant):
    del plant_info[plant][1:]
    return plant_info


def solution(plant_info):
    while True:
        command = input().split(': ')
        if command[0] == 'Exhibition':
            break
        info = command[1].split(' - ')
        if info[0] in plant_info:
            if command[0] == 'Rate':
                plant, rating = info[0], int(info[1])
                plant_info = rate(plant_info, plant, rating)
            elif command[0] == 'Update':
                plant, new_rarity = info[0], int(info[1])
                plant_info = update(plant_info, plant, new_rarity)
            elif command[0] == 'Reset':
                plant = info[0]
                plant_info = reset(plant_info, plant)
        else:
            print('error')
    return plant_info


def main(n):
    plant_info = {}
    for plant in range(n):
        line = input().split('<->')
        plant_info[line[0]] = [int(line[1])]
    result = solution(plant_info)
    print(f'Plants for the exhibition:')
    for key, value in result.items():
        if len(value[1:]):
            average_rating = sum(value[1:]) / (len(value) - 1)
        else:
            average_rating = 0
        print(f'- {key}; Rarity: {value[0]}; Rating: {average_rating:.2f}')


num_of_plants = int(input())
main(num_of_plants)
