animals_queue = input().split(', ')

if animals_queue[-1] == 'sheep':
    print(f'Oi! Sheep number {len(animals_queue) - 1}! You are about to be eaten by a wolf!')
else:
    print('Please go away and stop eating my sheep')

