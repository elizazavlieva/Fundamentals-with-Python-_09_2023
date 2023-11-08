submissions = {}
contest_users = {}

while True:
    command = input()
    if command == 'no more time':
        break

    username, contest, point = command.split(' -> ')
    points = int(point)
    if contest not in submissions:
        submissions[contest] = {username: points}
    elif username not in submissions[contest]:
        submissions[contest][username] = points
    elif submissions[contest][username] < points:
        submissions[contest][username] = points
    if username not in contest_users:
        contest_users[username] = {contest: points}
    elif contest not in contest_users[username]:
        contest_users[username][contest] = points
    elif contest_users[username][contest] < points:
        contest_users[username][contest] = points

for key, value in submissions.items():
    counter = 1
    print(f'{key}: {len(value)} participants')
    sorted_submissions = dict(sorted(value.items(), key= lambda x: (-x[1], x[0])))
    for k, v in sorted_submissions.items():
        print(f'{counter}. {k} <::> {v}')
        counter += 1
print('Individual standings:')
sorted_users = dict(sorted(contest_users.items(), key=lambda x: (-sum(x[1].values()), x[0])))
counter = 1
for k, v in sorted_users.items():
    print(f'{counter}. {k} -> {sum(v.values())}')
    counter += 1
