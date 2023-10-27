def solution(sequence_of_elements):
    moves = 0
    while True:
        if len(sequence_of_elements) == 0:
            print(f'You have won in {moves} turns!')
            break
        command = input().split()
        if command[0] == 'end':
            print(f"Sorry you lose :(")
            print(' '.join(sequence_of_elements))
            break
        index_one = int(command[0])
        index_two = int(command[1])
        moves += 1
        if index_one == index_two or index_one < 0 or index_two < 0 \
                or index_one >= len(sequence_of_elements) or index_two >= len(sequence_of_elements):
            print('Invalid input! Adding additional elements to the board')
            middle_index = len(sequence_of_elements) // 2
            sequence_of_elements.insert(middle_index, f'-{moves}a')
            sequence_of_elements.insert(middle_index, f'-{moves}a')
        elif sequence_of_elements[index_one] == sequence_of_elements[index_two]:

            print(f'Congrats! You have found matching elements - {sequence_of_elements[index_one]}!')
            removed_element = sequence_of_elements.pop(index_one)
            sequence_of_elements.remove(removed_element)
        elif sequence_of_elements[index_one] != sequence_of_elements[index_two]:
            print('Try again!')


elements = input().split()
solution(elements)

