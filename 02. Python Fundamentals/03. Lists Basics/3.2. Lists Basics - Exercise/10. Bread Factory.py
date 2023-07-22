events = input().split('|')

energy = 100
coins = 100

has_completed = True

for event in events:
    tokens = event.split('-')
    event_or_ingredient = tokens[0]
    number = int(tokens[1])
    
    if event_or_ingredient == 'rest':
        gained_energy = 0
 
        if energy + number > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += number
            gained_energy = number
 
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient == 'order':
        if energy >= 30:
            coins += number
            energy -= 30
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f'You bought {event_or_ingredient}.')
        else:
            print(f'Closed! Cannot afford {event_or_ingredient}.')
            has_completed = False
            break
        
if has_completed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
