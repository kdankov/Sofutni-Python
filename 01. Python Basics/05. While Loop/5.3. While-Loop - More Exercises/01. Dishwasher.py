detergent_bottles_count = int(input())

detergent = detergent_bottles_count * 750

days_count = 1
dishes = 0
pots = 0

while detergent >= 0:
    current_input = input()
    
    if current_input == 'End':
        break
    
    if days_count % 3 == 0:
        detergent -= int(current_input) * 15
        pots += int(current_input)
    else:
        detergent -= int(current_input) * 5
        dishes += int(current_input)
    
    days_count += 1
        
if detergent >= 0:
    print(f'Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
else:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')