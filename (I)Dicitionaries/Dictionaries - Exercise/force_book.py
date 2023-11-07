force_book = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if '|' in command:
        force_side, force_user = command.split(' | ')
        is_in_force = False
        for value in force_book.values():
            if force_user in value:
                is_in_force = True
        if not is_in_force:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)

        print(f'{force_user} joins the {force_side} side!')


for k, v in force_book.items():
    if len(v) > 0:
        print(f'Side: {k}, Members: {len(v)}')
        for i in v:
            print(f'! {i}')
