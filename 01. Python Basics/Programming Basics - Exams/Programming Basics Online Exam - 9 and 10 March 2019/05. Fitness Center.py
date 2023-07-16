fitness_visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0


for i in range(fitness_visitors):
    current_input = input()
    
    if current_input == 'Back':
        back += 1
    elif current_input == 'Chest':
        chest += 1
    elif current_input == 'Legs':
        legs += 1
    elif current_input == 'Abs':
        abs += 1
    elif current_input == 'Protein shake':
        protein_shake += 1
    elif current_input == 'Protein bar':
        protein_bar += 1
    
work_out_percentage = (back + chest + legs + abs) / fitness_visitors * 100
protein_percentage = (protein_bar + protein_shake) / fitness_visitors * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{work_out_percentage:.2f}% - work out')
print(f'{protein_percentage:.2f}% - protein')

