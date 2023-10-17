matrix = [[x for x in input().split()] for row in range(6)]

position = [int(x) for x in input() if x.isalnum()]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()

while command != 'Stop':
    tokens = command.split(', ')
    operation = tokens[0]
    direction = tokens[1]

    move = possible_moves[direction]
    row = position[0] + move[0]
    col = position[1] + move[1]

    if operation == 'Create':
        value = tokens[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value

    elif operation == 'Update':
        value = tokens[2]

        if matrix[row][col] != '.':
            matrix[row][col] = value

    elif operation == 'Delete':
        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    elif operation == 'Read':
        if matrix[row][col] != '.':
            print(matrix[row][col])

    position = [row, col]
    command = input()

[print(*row, sep=' ') for row in matrix]