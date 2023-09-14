team = input()
matches_count = int(input())

points = 0

wins = 0
draws = 0
losses = 0

for match in range(matches_count):
    current_match = input()
    
    if current_match == 'W':
        points += 3
        wins += 1
    elif current_match == 'D':
        points += 1
        draws += 1
    elif current_match == 'L':
        losses += 1


if matches_count > 0:
    win_rate = wins * 100 / matches_count
    
    print(f'{team} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {losses}')
    print(f'Win rate: {win_rate:.2f}%')
else:
    print(f'{team} hasn\'t played any games during this season.')