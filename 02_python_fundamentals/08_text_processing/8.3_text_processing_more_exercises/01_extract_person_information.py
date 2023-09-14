n = int(input())

for i in range(n):
    current_line = input()
    
    name_start_index = current_line.index('@')
    name_end_index = current_line.index('|')
    
    age_start_index = current_line.index('#')
    age_end_index = current_line.index('*')

    name = current_line[name_start_index + 1: name_end_index]
    age = current_line[age_start_index + 1: age_end_index]
    
    print(f'{name} is {age} years old.')
        

