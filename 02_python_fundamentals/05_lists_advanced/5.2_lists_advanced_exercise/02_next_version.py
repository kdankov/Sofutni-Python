current_version = [int(x) for x in input().split('.')]

current_version[2] += 1

if current_version[2] == 10:
    current_version[2] = 0
    current_version[1] += 1
    
    if current_version[1] == 10:
        current_version[1] = 0
        current_version[0] += 1
        
print('.'.join(str(x) for x in current_version))

