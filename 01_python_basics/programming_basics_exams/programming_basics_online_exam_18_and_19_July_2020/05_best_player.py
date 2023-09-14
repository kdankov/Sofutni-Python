player_name = input()

has_scored_hat_trick = False

best_player = {
    'name': '',
    'goals': 0
}

while player_name != 'END':
    goals_scored = int(input())
    
    if goals_scored > best_player['goals']:
        best_player['name'] = player_name
        best_player['goals'] = goals_scored
        
    if goals_scored >= 3:
        has_scored_hat_trick = True

    if goals_scored >= 10:
        break

    player_name = input()

print(f'{best_player["name"]} is the best player!')

if has_scored_hat_trick:
    print(f'He has scored {best_player["goals"]} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player["goals"]} goals.')