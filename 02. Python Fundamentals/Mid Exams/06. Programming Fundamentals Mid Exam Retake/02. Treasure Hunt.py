treasure_chest = input().split('|')

command = input()

while command != 'Yohoho!':
    args = command.split()
    action = args[0]
    
    if action == 'Loot':
        for i in range(1, len(args)):
            if args[i] not in treasure_chest:
                treasure_chest.insert(0, args[i])
    elif action == 'Drop':
        index = int(args[1])
        
        if 0 <= index < len(treasure_chest):
            item = treasure_chest.pop(index)
            treasure_chest.append(item)
    elif action == 'Steal':
        count = int(args[1])
        
        stolen_items = []
        
        if count < len(treasure_chest):
            stolen_items = treasure_chest[len(treasure_chest) - count:]
            treasure_chest = treasure_chest[:len(treasure_chest) - count]
        else:
            stolen_items = treasure_chest
            treasure_chest = []
        
        print(', '.join(stolen_items))
    
    command = input()  
    
if len(treasure_chest) > 0:
    print(f'Average treasure gain: {sum([len(x) for x in treasure_chest]) / len(treasure_chest):.2f} pirate credits.')
else:
    print(f'Failed treasure hunt.')