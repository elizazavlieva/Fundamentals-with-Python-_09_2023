people_in_queue = int(input())
people= people_in_queue
lift = [int(num) for num in input().split()]
empty_seats = len(lift) * 4 - sum(lift)

for position in lift:
    if position < 4 <= people_in_queue:
        count = 4-position
        people_in_queue -= count
        lift[lift.index(position)] = 4
    elif position < 4 and people_in_queue < 4 :
        lift[lift.index(position)] = position + people_in_queue
        people_in_queue = 0
        break


if people_in_queue > 0:
    print(f'There isn\'t enough space! {people_in_queue} people in a queue!')
elif people_in_queue == 0 and empty_seats > people :
    print(f'The lift has empty spots!')

print(' '.join([str(num) for num in lift]))

