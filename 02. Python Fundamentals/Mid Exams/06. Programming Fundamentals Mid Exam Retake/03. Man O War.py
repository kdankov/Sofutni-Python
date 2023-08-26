pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
maximum_health = int(input())

command = input()

while command != 'Retire':
    args = command.split()
    action = args[0]
    
    if action == 'Fire':
        index = int(args[1])
        damage = int(args[2])
        
        if 0 <= index < len(warship):
            warship[index] -= damage
            
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                exit()
    elif action == 'Defend':
        start_index = int(args[1])
        end_index = int(args[2])
        damage = int(args[3])
        
        if 0 <= start_index <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    exit()
    elif action == 'Repair':
        index = int(args[1])
        health = int(args[2])
        
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health
    elif action == 'Status':
        print(f'{len([x for x in pirate_ship if x < maximum_health * 0.2])} sections need repair.')

    command = input()
    
pirate_ship_status = sum(pirate_ship)
warship_status = sum(warship)

print(f'Pirate ship status: {pirate_ship_status}')
print(f'Warship status: {warship_status}')