n = int(input())

battlefield = []
submarine_position = []

CRUISERS_COUNT = 3
mines_hit = 0
cruisers_hit = 0

for row in range(n):
    battlefield.append(list(input()))
    for col in range(n):
        if battlefield[row][col] == 'S':
            submarine_position = [row, col]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    if mines_hit == 3:
        print(f'Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!')
        break

    if cruisers_hit == CRUISERS_COUNT:
        print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
        break

    command = input()
    next_move = possible_moves[command]

    desired_row = submarine_position[0] + next_move[0]
    desired_col = submarine_position[1] + next_move[1]

    if battlefield[desired_row][desired_col] == '*':
        mines_hit += 1
    elif battlefield[desired_row][desired_col] == 'C':
        cruisers_hit += 1
    elif battlefield[desired_row][desired_col] == '-':
        pass

    battlefield[submarine_position[0]][submarine_position[1]] = '-'
    battlefield[desired_row][desired_col] = 'S'
    submarine_position = [desired_row, desired_col]

[print(*row, sep='') for row in battlefield]