destinations = input()

current_line = input()

while current_line != 'Travel':
    tokens = current_line.split(':')
    operation = tokens[0]
    
    if operation == 'Add Stop':
        index = int(tokens[1])
        text = tokens[2]
        
        if 0 <= index < len(destinations):
            destinations = destinations[:index] + text + destinations[index:]
    
    elif operation == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        
        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
            destinations = destinations[:start_index] + destinations[end_index + 1:]
    
    elif operation == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]
        
        destinations = destinations.replace(old_string, new_string)
        
    print(destinations)
    
    current_line = input()

print(f'Ready for world tour! Planned stops: {destinations}')