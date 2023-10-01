matrix = []
shooter_position = []
targets_count = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            shooter_position = [row, col]
        elif matrix[row][col] == 'x':
            targets_count += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

shot_targets_positions = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'shoot':
        r = shooter_position[0] + directions[command[1]][0]
        c = shooter_position[1] + directions[command[1]][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets_count -= 1
                shot_targets_positions.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]

        if targets_count <= 0:
            print(f'Training completed! All {len(shot_targets_positions)} targets hit.')
            break
    elif command[0] == 'move':
        direction = command[1]
        steps = int(command[2])
        r = shooter_position[0] + (directions[direction][0] * steps)
        c = shooter_position[1] + (directions[direction][1] * steps)
        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[shooter_position[0]][shooter_position[1]] = '.'
            shooter_position = [r, c]

if targets_count > 0:
    print(f'Training not completed! {targets_count} targets left.')

[print(row) for row in shot_targets_positions]