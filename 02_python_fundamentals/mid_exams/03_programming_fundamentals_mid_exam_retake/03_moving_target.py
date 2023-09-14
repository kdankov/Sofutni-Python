targets = [int(x) for x in input().split()]

command = input()

while command != 'End':
    args = command.split()
    action = args[0]
    index = int(args[1])
    
    if action == 'Shoot':
        power = int(args[2])
        
        if 0 <= index < len(targets):
            targets[index] -= power
            
            if targets[index] <= 0:
                targets.pop(index)
        
    elif action == 'Add':
        value = int(args[2])
        
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif action == 'Strike':
        radius = int(args[2])
        
        if index - radius >= 0 and index + radius < len(targets):
            del targets[index - radius:index + radius + 1]
        else:
            print('Strike missed!')
    
    command = input()
    
print('|'.join([str(x) for x in targets]))