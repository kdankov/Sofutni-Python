won_games = 0
lost_games = 0
total_games_count = 0

tournament_name = input()

while tournament_name != 'End of tournaments':
    matches_count = int(input())
    for i in range(1, matches_count + 1):
        total_games_count += 1
        
        first_team_points = int(input())
        second_team_points = int(input())
        
        if first_team_points > second_team_points:
            won_games += 1
            print(f'Game {i} of tournament {tournament_name}: win with {first_team_points - second_team_points} points.')
        else:
            lost_games += 1
            print(f'Game {i} of tournament {tournament_name}: lost with {second_team_points - first_team_points} points.')
        
    tournament_name = input()
    
won_games = won_games / total_games_count * 100
lost_games = lost_games / total_games_count * 100

print(f'{won_games:.2f}% matches win')
print(f'{lost_games:.2f}% matches lost')