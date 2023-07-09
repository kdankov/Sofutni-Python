from math import ceil

wall_height = int(input())
wall_width = int(input())
percent = int(input())

total = wall_height * wall_width * 4
to_paint = ceil(total - total * 1.0 * percent / 100);

liters_paint = input()

while liters_paint != 'Tired!':
    liters_paint = int(liters_paint)
    
    to_paint -= liters_paint
    
    if to_paint <= 0:
        break
    
    liters_paint = input()
    
if to_paint == 0:
    print('All walls are painted! Great job, Pesho!')
elif to_paint > 0:
    print(f'{to_paint} quadratic m left.')
else:
    print(f'All walls are painted and you have {abs(to_paint)} l paint left!')