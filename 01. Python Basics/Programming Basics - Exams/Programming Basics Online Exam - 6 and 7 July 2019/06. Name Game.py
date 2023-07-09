name = input()

winner = {
    "name": '',
    "points": 0
}

while name != 'Stop':
    current_points = 0
    for i in name:
        num = int(input())
        
        if num == ord(i):
            current_points += 10
        else:
            current_points += 2
    
    if current_points >= winner['points']:
        winner['name'] = name
        winner['points'] = current_points
    
    name = input()
print(f'The winner is {winner["name"]} with {winner["points"]} points!')