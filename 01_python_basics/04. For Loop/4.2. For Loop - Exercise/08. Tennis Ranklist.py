from math import floor

tournaments_count = int(input())
starting_points = int(input())

total_points = starting_points

average_points = 0
tournamets_won_average = 0

for i in range(tournaments_count):
    stage = input()
    
    if stage == 'W':
        total_points += 2000
        average_points += 2000
        tournamets_won_average += 1
    elif stage == 'F':
        total_points += 1200
        average_points += 1200
    elif stage == 'SF':
        total_points += 720
        average_points += 720
        
average_points /= tournaments_count

tournamets_won_average = (tournamets_won_average / tournaments_count) * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(average_points)}')
print(f'{tournamets_won_average:.2f}%')
