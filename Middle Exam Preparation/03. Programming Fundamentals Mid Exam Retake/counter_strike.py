initial_energy = int(input())
current_energy = initial_energy
counter = 0
while True:
    command = input()
    if command == 'End of battle':
        print(f'Won battles: {counter}. Energy left: {current_energy}')
        break
    distance = int(command)
    if current_energy >= distance:
        current_energy -= distance
        counter += 1

    else:
        print(f'Not enough energy! Game ends with {counter} '
              f'won battles and {current_energy} energy')
        break
    if counter % 3 == 0:
        current_energy += counter

