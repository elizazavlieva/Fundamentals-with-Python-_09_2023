def ship_field(rows):
    field = []
    for i in range(rows):
        ship = [int(num) for num in input().split()]
        field.append(ship)
    return field


def destroyed_ships(rows):

    battlefield = ship_field(rows)
    attack = [num for num in input().split()]
    counter = 0
    for i in attack:
        row = int(i[0])
        col = int(i[2])
        for index, item in enumerate(battlefield[row]):
            if index == col:
                if item > 0:
                    battlefield[row][index] -= 1
                    if battlefield[row][index] <= 0:
                        counter += 1

    return counter


n = int(input())
print(destroyed_ships(n))