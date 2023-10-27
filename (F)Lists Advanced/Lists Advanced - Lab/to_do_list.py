def progress_todo_list():
    todo_list = []
    while True:
        command = input()
        if command == 'End':
            break
        todo_list.append(command)
    sorted_notes = sorted(todo_list, key=lambda x: int(x.split('-')[0]))
    return [item.split('-')[1] for item in sorted_notes]


print(progress_todo_list())