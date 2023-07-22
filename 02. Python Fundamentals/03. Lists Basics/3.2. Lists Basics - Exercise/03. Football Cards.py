cards = input().split(' ')

team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

game_terminated = False

for card in cards:
    current_card = card.split('-')
    current_team = current_card[0]
    current_number = int(current_card[1])
    
    if current_team == 'A':
        if current_number in team_A:
            team_A.remove(current_number)
    elif current_team == 'B':
        if current_number in team_B:
            team_B.remove(current_number)
    
    if len(team_A) < 7 or len(team_B) < 7:
        game_terminated = True
        break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')

if game_terminated:
    print('Game was terminated')
