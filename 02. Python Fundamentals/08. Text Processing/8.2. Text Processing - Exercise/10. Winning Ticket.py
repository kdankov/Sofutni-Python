tickets = [x.strip() for x in input().split(', ')]

count = 0
symbol = ''

def check_count(symbol, first, second):
    total_count = 6
    for i in range(7, 11):
        if (i * symbol) in first and (i * symbol) in second:
            total_count += 1
    return total_count

for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    
    first_half = ticket[0:int(len(ticket) / 2)]
    second_half = ticket[int(len(ticket) / 2):]
    
    if (6 * '@') in first_half and (6 * '@') in second_half:
        count = check_count('@', first_half, second_half)
        symbol = '@'
    elif (6 * '$') in first_half and (6 * '$') in second_half:
        count = check_count('$', first_half, second_half)
        symbol = '$'
    elif (6 * '#') in first_half and (6 * '#') in second_half:
        count = check_count('#', first_half, second_half)
        symbol = '#'
    elif (6 * '^') in first_half and (6 * '^') in second_half:
        count = check_count('^', first_half, second_half)
        symbol = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue
        
    if count != 10:
        print(f'ticket "{ticket}" - {count}{symbol}')
    else:
        print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')