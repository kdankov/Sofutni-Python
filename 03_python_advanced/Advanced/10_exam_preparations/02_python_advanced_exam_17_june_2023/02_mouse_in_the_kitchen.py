rows, cols = (int(x) for x in input().split(','))

matrix = []
mouse_position = []
cheese_pieces = 0

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse_position = [row, col]
        elif matrix[row][col] == 'C':
            cheese_pieces += 1

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while cheese_pieces != 0:
    command = input()

    if command == 'danger':
        print('Mouse will come back later!')
        break

    move = possible_moves[command]
    row = mouse_position[0] + move[0]
    col = mouse_position[1] + move[1]

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print('No more cheese for tonight!')
        break

    if matrix[row][col] == 'C':
        cheese_pieces -= 1
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [row, col]
        matrix[mouse_position[0]][mouse_position[1]] = 'M'

    if matrix[row][col] == '@':
        continue

    if matrix[row][col] == 'T':
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [row, col]
        matrix[mouse_position[0]][mouse_position[1]] = 'M'
        print('Mouse is trapped!')
        break

    if matrix[row][col] == '*':
        matrix[mouse_position[0]][mouse_position[1]] = '*'
        mouse_position = [row, col]
        matrix[mouse_position[0]][mouse_position[1]] = 'M'
        continue
else:
    print('Happy mouse! All the cheese is eaten, good night!')

[print(*row, sep='') for row in matrix]