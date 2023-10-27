n = int(input())
total_free_chairs = 0
is_enough = True
for room in range(1, n + 1):
    command = input().split()
    people = int(command[1])
    chairs = len(command[0])
    if chairs < people:
        needed_chairs_in_room = abs(people - chairs)
        print(f'{needed_chairs_in_room} more chairs needed in room {room}' )
        is_enough = False
    else:

        total_free_chairs += abs(people - chairs)
if is_enough:
    print(f'Game On, {total_free_chairs} free chairs left')