groceries = input().split('!')

command = input()

while command != 'Go Shopping!':
    args = command.split()
    action = args[0]
    
    if action == 'Urgent':
        item = args[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif action == 'Unnecessary':
        item = args[1]
        
        if item in groceries:
            groceries.remove(item)
    elif action == 'Correct':
        old_item = args[1]
        new_item = args[2]
        
        groceries = [new_item if item == old_item else item for item in groceries]
    elif action == 'Rearrange':
        item = args[1]
        
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
    
    command = input()
    
    
print(', '.join(groceries))