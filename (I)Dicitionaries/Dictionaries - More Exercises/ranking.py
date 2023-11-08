
contest_info = {}
users_score = {}
while True:
    command = input()
    if command == 'end of contests':
        break
    competition, contest_password = command.split(':')
    if competition not in contest_info:
        contest_info[competition] = contest_password


while True:
    user_input = input()

    if user_input == 'end of submissions':
        break
    contest, password, username, points = user_input.split('=>')
    points = int(points)
    if contest in contest_info.keys():
        if contest_info[contest] == password:
            if username not in users_score.keys():
                users_score[username] = {}
                users_score[username][contest] = points
            elif username in users_score.keys():
                if contest not in users_score[username].keys():
                    users_score[username][contest] = points
                else:
                    is_valid = False
                    for k,v in users_score.items():
                        if k == username:
                            for course, score in v.items():
                                if course == contest and score < points:
                                    is_valid = True
                                    break
                        if is_valid:
                            break
                    if is_valid:
                        users_score[username][contest] = points

users_score = dict(sorted(users_score.items()))
v = []
for key, value in users_score.items():
    v = sorted(value.items(), key= lambda x:x[1], reverse=True)
    users_score[key]= dict(v)

winner = ''
winner_score = 0

for k, v in users_score.items():
    if sum(v.values()) > winner_score:
        winner = k
        winner_score = sum(v.values())
print(f'Best candidate is {winner} with total {winner_score} points.')
print('Ranking:')
for k,v in users_score.items():
    print(f'{k}')
    for course, score in v.items():
        print(f'#  {course} -> {score}')
