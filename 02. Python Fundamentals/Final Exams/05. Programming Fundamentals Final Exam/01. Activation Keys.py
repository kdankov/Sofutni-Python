raw_activation_key = input()

current_line = input()

while current_line != 'Generate':
    tokens = current_line.split('>>>')
    command = tokens[0]
    
    if command == 'Contains':
        substring = tokens[1]
        
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')
            
    elif command == 'Flip':
        case = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        
        if case == 'Upper':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        elif case == 'Lower':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]
        
        print(raw_activation_key)
        
    elif command == 'Slice':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        
        print(raw_activation_key)
    
    current_line = input()
    
print(f' Your activation key is: {raw_activation_key}')