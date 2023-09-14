easter_breads_count = int(input())

winner = {
    'name': '',
    'points': 0
}

for i in range(easter_breads_count):
    chef_name = input()
    current_chef_points = 0
    
    points = input()
    while points != 'Stop':
        current_chef_points += int(points)
        
        points = input()
        
    print(f'{chef_name} has {current_chef_points} points.')
    
    if current_chef_points > winner['points']:
        winner['name'] = chef_name
        winner['points'] = current_chef_points
        
        print(f'{chef_name} is the new number 1!')
        
print(f'{winner["name"]} won competition with {winner["points"]} points!')
