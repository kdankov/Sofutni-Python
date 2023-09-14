gifts_to_buy = input().split(' ')

command = input()

while command != 'No Money':
    tokens = command.split(' ')
    action = tokens[0]
    current_gift = tokens[1]
    
    if action == 'OutOfStock':
        gifts_to_buy = ['None' if gift == current_gift else gift for gift in gifts_to_buy]
    elif action == 'Required':
        index = int(tokens[2])
        if 0 <= index <= len(gifts_to_buy):
            gifts_to_buy[index] = current_gift
    elif action == 'JustInCase':
        gifts_to_buy[-1] = current_gift
        
    command = input()

print(' '.join(gift for gift in gifts_to_buy if gift != 'None'))
