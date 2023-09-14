fire = input().split('#')
available_water = int(input())

cells = []
effort = 0

for i in fire:
    tokens = i.split(' = ')
    fire_type = tokens[0]
    cell_value = int(tokens[1])
    
    is_valid = False
    
    if available_water < cell_value:
        continue
    
    if fire_type == 'High':
        if 81 <= cell_value <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= cell_value <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= cell_value <= 50:
            is_valid = True
    
    if is_valid:
        available_water -= cell_value
        cells.append(cell_value)
        effort += cell_value * 0.25
        
print('Cells:')
for cell in cells:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')