players_pool = {}
while True:
    command = input()
    if command == 'Season end':
        break
    if ' -> ' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in players_pool:
            players_pool[player] = {position: skill}
        elif position not in players_pool[player]:
            players_pool[player][position] = skill
        elif players_pool[player][position] < skill:
            players_pool[player][position] = skill

    elif ' vs ' in command:
        player_one, player_two = command.split(' vs ')
        if (player_one in players_pool) and (player_two in players_pool):
            removed_player = None
            for pos_one in players_pool[player_one].keys():
                for pos_two in players_pool[player_two].keys():
                    if pos_two == pos_one:
                        total_skill_player_one = sum(players_pool[player_one].values())
                        total_skill_player_two = sum(players_pool[player_two].values())
                        if total_skill_player_one > total_skill_player_two:
                            removed_player = player_two
                        elif total_skill_player_one < total_skill_player_two:
                            removed_player = player_one
            if removed_player:
                players_pool.pop(removed_player)


sorted_skills = dict(sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for key, value in sorted_skills.items():
    if len(sorted_skills[key]) > 0:
        print(f'{key}: {sum(value.values())} skill')
        sorted_users = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
        for k, v in sorted_users.items():
            print(f'- {k} <::> {v}')