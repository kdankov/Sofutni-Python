targets = [int(x) for x in input().split()]

command = input()

while command != 'End':
    index = int(command)
    
    if 0 <= index < len(targets):
        if targets[index] != -1:
            target_value = targets[index]
            targets[index] = -1
            for index, value in enumerate(targets):
                if value != -1:
                    if value > target_value:
                        targets[index] -= target_value
                    else:
                        targets[index] += target_value
    
    command = input()   
    
print(f'Shot targets: {len([x for x in targets if x == -1])} -> {" ".join([str(x) for x in targets])}')
    