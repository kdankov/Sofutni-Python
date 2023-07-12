seats = int(input())

income = 0

command = input()

is_full = False

while command != 'Movie time!':
    current_seats = int(command)
    
    if current_seats > seats:
        is_full = True
        break
    
    seats -= current_seats
    income += current_seats * 5
    
    if current_seats % 3 == 0:
        income -= 5
        
    command = input()
    
if is_full:
    print('The cinema is full.')
else:
    print(f'There are {seats} seats left in the cinema.')
    
print(f'Cinema income - {income} lv.')