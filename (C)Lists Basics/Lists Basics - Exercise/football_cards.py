team_A = 11
team_B = 11
last_player_A = ''
last_player_b = ''
red_cards = input()
my_list = red_cards.split(' ')
is_terminated = False
for i in my_list:
    if 'A' in i:
        if i == last_player_A:
            continue
        else:
            last_player_A = i
            team_A -= 1

    elif 'B' in i:
        if i == last_player_b:
            continue
        else:
            last_player_b = i
            team_B -= 1
    if team_B < 7 or team_A < 7:
        is_terminated = True
        break

print(f'Team A - {team_A}; Team B - {team_B}')
if is_terminated:
    print('Game was terminated')