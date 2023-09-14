player_name = input()

field = input()

successful_shots = 0
unsuccessful_shots = 0

has_won = False

points = 301

while field != 'Retire':
    current_points = int(input())
    
    if field == 'Single':
        if current_points > points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points -= current_points
    elif field == 'Double':
        if current_points * 2 > points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points -= current_points * 2
    elif field == 'Triple':
        if current_points * 3 > points:
            unsuccessful_shots += 1
        else:
            successful_shots += 1
            points -= current_points * 3
    
    if points == 0:
        has_won = True
        break
        
    field = input()

if has_won:
    print(f'{player_name} won the leg with {successful_shots} shots.')
else:
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
