def kate_position(maze):
    position = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'k':
                position.append(row)
                position.append(col)
    return position


def available_movement(maze):
    total_free_space = []

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            is_space = False
            section = []
            if maze[row][col] == ' ':
                section.append(row)
                section.append(col)
                is_space = True
            if is_space:
                total_free_space.append(section)
    return total_free_space


def escape(position, movements, maze):

    step = 0
    moves = 0

    while True:
        move = []
        if len(movements) <= step:
            break

        move.append(movements[step][0])
        move.append(movements[step][1])
        if move[0] == position[0] and position[1] - move[1] == 1:
            position = move
            moves += 1
            movements.pop(step)
            step = 0
        elif move[0] == position[0] and move[1] - position[1] == 1:
            position = move
            moves += 1
            movements.pop(step)
            step = 0
        elif move[0] - position[0] == 1 and position[1] == move[1]:
            position = move
            moves += 1
            movements.pop(step)
            step = 0
        elif position[0] - move[0] == 1 and position[1] == move[1]:
            position = move
            moves += 1
            movements.pop(step)
            step = 0
        else:
            step += 1
    if position[0] == 0 or position[0] == (len(maze) - 1) or position[1] == 0 or position[1] == len(maze[0]):
        return f'Kate got out in {moves + 1} moves'
    return f'Kate cannot get out'


n = int(input())
maze_map = []
for i in range(n):
    maze_map.append(input())
print(escape(kate_position(maze_map), available_movement(maze_map), maze_map))