journal = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break

    elif command[0] == 'Collect':
        for i in journal:
            if command[1] in journal:
                continue
            else:
                journal.append(command[1])
    elif command[0] == 'Drop':
        for item, index in enumerate(journal):
            if command[1] == index:
                journal.pop(item)
    elif command[0] == 'Combine Items':
        old_item, new_item = command[1].split(':')
        for position, item in enumerate(journal):
            if old_item == item:
                journal.insert(position + 1, new_item)
    elif command[0] == 'Renew':
        for item, index in enumerate(journal):
            if index == command[1]:
                popped_item = journal.pop(item)
                journal.append(popped_item)
print(', '.join(journal))