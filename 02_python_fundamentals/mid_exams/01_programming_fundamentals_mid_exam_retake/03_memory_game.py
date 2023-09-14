elements = input().split()

command = input()

moves_count = 0

has_won = False

while command != 'end':
    args = command.split()
    first_index = int(args[0])
    second_index = int(args[1])
    
    moves_count += 1
    
    if first_index == second_index or 0 > first_index or first_index > len(elements) - 1 or 0 > second_index or second_index > len(elements) - 1:
        elements.insert(len(elements) // 2, f'-{moves_count}a')
        elements.insert(len(elements) // 2, f'-{moves_count}a')
        print(f'Invalid input! Adding additional elements to the board')
    elif elements[first_index] == elements[second_index]:
        matching_elements = elements[first_index]
        elements = [el for el in elements if el != matching_elements]
        
        print(f'Congrats! You have found matching elements - {matching_elements}!')
    elif elements[first_index] != elements[second_index]:
        print(f'Try again!')
    
    if len(elements) == 0:
        has_won = True
        break
        
    command = input()
    
if has_won:
    print(f'You have won in {moves_count} turns!')
else:
    print(f'Sorry you lose :(')
    print(' '.join(elements))