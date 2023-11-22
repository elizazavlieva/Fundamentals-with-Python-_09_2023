stops = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        index, place = int(command[1]), command[2]
        if 0 <= index <= len(stops):
            stops = ''.join((stops[:index], place, stops[index:]))
    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops.replace(stops[start_index:end_index+1], '')

    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
