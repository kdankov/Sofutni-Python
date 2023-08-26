dungeons_rooms = input().split('|')

health = 100
bitcoins = 0

for i in range(len(dungeons_rooms)):
    room = dungeons_rooms[i].split()
    command = room[0]
    number = int(room[1])
    
    if command == 'potion':
        if health + number >= 100:
            print(f'You healed for {100 - health} hp.')
            health = 100
        else:
            print(f'You healed for {number} hp.')
            health += number
            
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i + 1}')
            exit()

print('You\'ve made it!')
print(f'Bitcoins: {bitcoins}')
print(f'Health: {health}')
