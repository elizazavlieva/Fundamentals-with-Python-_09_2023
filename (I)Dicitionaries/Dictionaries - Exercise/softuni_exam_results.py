results = {}
submission = {}
is_banned = False
username, language, points = None, None, None
while True:
    command = input().split('-')
    if command[0] == 'exam finished':
        break
    if len(command) > 2:
        username, language, points = command[0], command[1], int(command[2])
    else:
        username = command[0]
        is_banned = True
    if language not in submission:
        submission[language] = 1
    else:
        submission[language] += 1
    if username not in results:
        results[username] = points
    else:
        if is_banned:
            results.pop(username)
            submission[language] -= 1
        else:
            if points > results[username]:
                results[username] = points

print('Results:')
for k, v in results.items():
    print(f'{k} | {v}')

print('Submissions:')
for k, v in submission.items():
    print(f'{k} - {v}')
