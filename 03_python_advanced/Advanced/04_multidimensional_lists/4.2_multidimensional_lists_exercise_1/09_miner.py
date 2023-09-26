def is_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


n = int(input())
commands = input().split()

matrix = []
curr_row, curr_col = 0, 0
coal = 0
game_over = False

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 's':
            curr_row, curr_col, = row, col,
        elif matrix[row][col] == 'c':
            coal += 1

for command in commands:
    if command == 'up':
        if is_valid(curr_row - 1, curr_col, n):
            curr_row -= 1
    elif command == 'down':
        if is_valid(curr_row + 1, curr_col, n):
            curr_row += 1
    elif command == 'left':
        if is_valid(curr_row, curr_col - 1, n):
            curr_col -= 1
    elif command == 'right':
        if is_valid(curr_row, curr_col + 1, n):
            curr_col += 1

    if matrix[curr_row][curr_col] == 'e':
        print(f'Game over! ({curr_row}, {curr_col})')
        game_over = True
        break
    elif matrix[curr_row][curr_col] == 'c':
        coal -= 1
        matrix[curr_row][curr_col] = '*'

        if coal == 0:
            print(f'You collected all coal! ({curr_row}, {curr_col})')
            game_over = True
            break

if not game_over:
    print(f'{coal} pieces of coal left. ({curr_row}, {curr_col})')