rows, cols = [int(x) for x in input().split()]

playground = []
blind_man_position = []

OPPONENTS_COUNT = 3

for row in range(rows):
    playground.append([x for x in input().split()])
    for col in range(cols):
        if playground[row][col] == 'B':
            blind_man_position = [row, col]

playground[blind_man_position[0]][blind_man_position[1]] = '-'

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

touched_opponents = 0
moves_count = 0

command = input()

while command != 'Finish':
    move = possible_moves[command]

    desired_row = blind_man_position[0] + move[0]
    desired_col = blind_man_position[1] + move[1]

    if desired_row < 0 or desired_row >= rows or desired_col < 0 or desired_col >= cols:
        command = input()
        continue
    elif playground[desired_row][desired_col] == 'O':
        command = input()
        continue
    elif playground[desired_row][desired_col] == '-':
        moves_count += 1
        blind_man_position = [desired_row, desired_col]
    elif playground[desired_row][desired_col] == 'P':
        touched_opponents += 1
        moves_count += 1
        playground[desired_row][desired_col] = '-'
        blind_man_position = [desired_row, desired_col]

        if touched_opponents == OPPONENTS_COUNT:
            break

    command = input()

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {moves_count}')