from statistics import mean 

n = int(input())

plants_dict = {}

for _ in range(n):
    current_plant = input().split('<->')
    plant_type = current_plant[0]
    plant_rarity = current_plant[1]
    
    if plant_type not in plants_dict:
        plants_dict[plant_type] = []
    plants_dict[plant_type] = [plant_rarity]
    
current_line = input()

while current_line != 'Exhibition':
    tokens = current_line.split()
    operation = tokens[0]
    plant = tokens[1]
    
    if operation == 'Rate:':
        rating = int(tokens[3])
        
        if plant in plants_dict:
            plants_dict[plant].append(rating)
        else:
            print('error')
            
    elif operation == 'Update:':
        new_rarity = tokens[3]
        
        if plant in plants_dict:
            plants_dict[plant][0] = new_rarity
        else:
            print('error')
            
    elif operation == 'Reset:':
        if plant in plants_dict:
            plants_dict[plant] = [plants_dict[plant][0]]
        else:
            print('error')

    current_line = input()
    
print(f'Plants for the exhibition:')

for k, v in plants_dict.items():
    if len(v) > 1:  
        print(f'- {k}; Rarity: {v[0]}; Rating: {sum(v[1:]) / len(v[1:]):.2f}')
    else:
        print(f'- {k}; Rarity: {v[0]}; Rating: 0.00')