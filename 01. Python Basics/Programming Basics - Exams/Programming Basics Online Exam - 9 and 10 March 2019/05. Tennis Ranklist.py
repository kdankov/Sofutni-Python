from math import floor

tournamets_count = int(input())
current_points = int(input())

average_points = 0
won_tournamets = 0

for i in range(tournamets_count):
    reached_stage = input()
    
    if reached_stage == 'W':
        current_points += 2000
        average_points += 2000
        won_tournamets += 1
    elif reached_stage == 'F':
        current_points += 1200
        average_points += 1200
    elif reached_stage == 'SF':
        current_points += 720
        average_points += 720
    
print(f'Final points: {current_points}')

average_points /= tournamets_count
print(f'Average points: {floor(average_points)}')

won_tournamets = won_tournamets / tournamets_count * 100
print(f'{won_tournamets:.2f}%')