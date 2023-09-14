games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for i in range(games_sold):
    current_game = input()
    
    if current_game == 'Hearthstone':
        hearthstone += 1
    elif current_game == 'Fornite':
        fornite += 1
    elif current_game == 'Overwatch':
        overwatch += 1
    else:
        others += 1
        
hearthstone = hearthstone * 100 / games_sold
fornite = fornite * 100 / games_sold
overwatch = overwatch * 100 / games_sold
others = others * 100 / games_sold

print(f'Hearthstone - {hearthstone:.2f}%')
print(f'Fornite - {fornite:.2f}%')
print(f'Overwatch - {overwatch:.2f}%')
print(f'Others - {others:.2f}%')