energy = int(input())

command = input()

not_enough_energy = False
won_battles = 0

while command != 'End of battle':
    distance = int(command)
    
    if energy - distance >= 0:
        energy -= distance
        won_battles += 1
    else:
        not_enough_energy = True
        break
    
    if won_battles % 3 == 0:
        energy += won_battles
        
    command = input()

if not_enough_energy:
    print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
else:
    print(f'Won battles: {won_battles}. Energy left: {energy}')