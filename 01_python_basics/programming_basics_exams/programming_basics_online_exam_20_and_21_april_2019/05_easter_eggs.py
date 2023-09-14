total_eggs_count = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_eggs = {
    'color': '',
    'count': 0
}

for i in range(total_eggs_count):
    current_egg = input()
    
    if current_egg == 'red':
        red_eggs += 1
        
        if red_eggs > max_eggs['count']:
            max_eggs['color'] = 'red'
            max_eggs['count'] = red_eggs
    
    elif current_egg == 'orange':
        orange_eggs += 1
        
        if orange_eggs > max_eggs['count']:
            max_eggs['color'] = 'orange'
            max_eggs['count'] = orange_eggs
            
    elif current_egg == 'blue':
        blue_eggs += 1
        
        if blue_eggs > max_eggs['count']:
            max_eggs['color'] = 'blue'
            max_eggs['count'] = blue_eggs
            
    elif current_egg == 'green':
        green_eggs += 1
        
        if green_eggs > max_eggs['count']:
            max_eggs['color'] = 'green'
            max_eggs['count'] = green_eggs

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_eggs["count"]} -> {max_eggs["color"]}')