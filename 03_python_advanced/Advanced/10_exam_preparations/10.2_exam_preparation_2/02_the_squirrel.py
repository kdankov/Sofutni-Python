n = int(input())

moves = input().split(', ')

collected_hazelnuts = 0
available_hazelnuts = 0
squirrel_position = []

field = []

flag = False

for row in range(n):
    field.append(list(input()))
    for col in range(n):
        if field[row][col] == 's':
            squirrel_position = [row, col]
        elif field[row][col] == 'h':
            available_hazelnuts += 1

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for direction in moves:
    current_move = possible_moves[direction]

    row = squirrel_position[0] + current_move[0]
    col = squirrel_position[1] + current_move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        print('The squirrel is out of the field.')
        flag = True
        break

    if field[row][col] == 'h':
        collected_hazelnuts += 1
        available_hazelnuts -= 1
        if collected_hazelnuts == 3:
            print(f'Good job! You have collected all hazelnuts!')
            flag = True
            break

        if available_hazelnuts == 0:
            break
    elif field[row][col] == '*':
        field[row][col] = '*'
        squirrel_position = [row, col]
        field[row][col] = 's'
        continue
    elif field[row][col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        flag = True
        break

    field[row][col] = '*'
    squirrel_position = [row, col]
    field[row][col] = 's'

if not flag:
    print(f'There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {collected_hazelnuts}')