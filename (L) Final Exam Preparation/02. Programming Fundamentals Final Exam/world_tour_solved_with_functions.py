def add_stop(destination, index, place):
    if 0 <= index < len(destination):
        return destination[:index] + place + destination[index:]
    else:
        return destination


def remove_stop(destination, start_index, end_index):
    if 0 <= start_index and end_index < len(destination):
        return destination.replace(destination[start_index:end_index + 1], '')
    else:
        return destination


def switch(destination, old_place, new_place):
    if old_place in destination:
        return destination.replace(old_place,new_place)
    else:
        return destination


def solution(destination):
    while True:
        command = input().split(':')
        if command[0] == 'Travel':
            print(f'Ready for world tour! Planned stops: {destination}')
            break
        elif command[0] == 'Add Stop':
            index, place = int(command[1]), command[2]
            destination = add_stop(destination, index, place)
            print(destination)
        elif command[0] == 'Remove Stop':
            start_index, end_index = int(command[1]), int(command[2])
            destination = remove_stop(destination, start_index, end_index)
            print(destination)
        elif command[0] == 'Switch':
            old_place, new_place = command[1], command[2]
            destination = switch(destination, old_place, new_place)
            print(destination)


line = input()
solution(line)
