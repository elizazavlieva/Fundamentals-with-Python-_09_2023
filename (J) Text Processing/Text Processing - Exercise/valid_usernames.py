usernames = input().split(', ')

for user in usernames:
    if 3 <= len(user) <= 16:
        is_valid = True
        for char in user:
            if not char.isalnum() and char != '-' and char != '_':
                is_valid = False
        if is_valid:
            print(user)
