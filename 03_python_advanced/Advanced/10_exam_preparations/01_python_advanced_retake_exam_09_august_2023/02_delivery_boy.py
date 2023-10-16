rows, cols = [int(x) for x in input().split()]

field = []
delivery_boy_starting_position = []
delivery_boy_current_position = []


for row in range(rows):
    field.append(list(input()))
    for col in range(cols):
        if field[row][col] == 'B':
            delivery_boy_starting_position = [row, col]
            delivery_boy_current_position = [row, col]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

is_late = False

while True:
    command = input()

    move = possible_moves[command]

    row = delivery_boy_current_position[0] + move[0]
    col = delivery_boy_current_position[1] + move[1]

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print('The delivery is late. Order is canceled.')
        field[delivery_boy_starting_position[0]][delivery_boy_starting_position[1]] = ' '
        is_late = True
        break

    if field[row][col] == 'P':
        field[row][col] = 'R'
        print('Pizza is collected. 10 minutes for delivery.')
    elif field[row][col] == '*':
        continue
    elif field[row][col] == 'A':
        field[row][col] = 'P'
        print('Pizza is delivered on time! Next order...')
        break
    elif field[row][col] == '-':
        field[row][col] = '.'
        delivery_boy_current_position = [row, col]
        continue

    delivery_boy_current_position = [row, col]

if not is_late:
    field[delivery_boy_starting_position[0]][delivery_boy_starting_position[1]] = 'B'

[print(*row, sep='') for row in field]