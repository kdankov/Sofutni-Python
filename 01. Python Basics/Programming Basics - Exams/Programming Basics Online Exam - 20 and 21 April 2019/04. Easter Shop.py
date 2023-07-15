eggs_count = int(input())

command = input()

not_enough = False

eggs_sold = 0

while command != 'Close':
    current_eggs_count = int(input())
    
    if command == 'Buy':
        if current_eggs_count > eggs_count:
            not_enough = True
            break
        else:
            eggs_count -= current_eggs_count
            eggs_sold += current_eggs_count
            
    elif command == 'Fill':
        eggs_count += current_eggs_count
    
    command = input()
    
if not_enough:
    print('Not enough eggs in store!')
    print(f'You can buy only {eggs_count}.')
else:
    print('Store is closed!')
    print(f'{eggs_sold} eggs sold.')