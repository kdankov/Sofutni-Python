from collections import deque

field = []
FIELD_SIZE = 6

rover_position = []
water_deposits = 0
metal_deposits = 0
concrete_deposits = 0

has_broken = False

for row in range(FIELD_SIZE):
    field.append(input().split())
    for col in range(FIELD_SIZE):
        if field[row][col] == 'E':
            rover_position = [row, col]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

moves = deque(input().split(', '))

while moves:
    current_move = possible_moves[moves.popleft()]
    rover_position[0] += current_move[0]
    rover_position[1] += current_move[1]

    if rover_position[0] < 0:
        rover_position[0] = 5
    elif rover_position[0] > 5:
        rover_position[0] = 0
    elif rover_position[1] < 0:
        rover_position[1] = 5
    elif rover_position[1] > 5:
        rover_position[1] = 0

    if field[rover_position[0]][rover_position[1]] == 'W':
        water_deposits += 1
        print(f'Water deposit found at ({rover_position[0]}, {rover_position[1]})')
        continue
    if field[rover_position[0]][rover_position[1]] == 'M':
        metal_deposits += 1
        print(f'Metal deposit found at ({rover_position[0]}, {rover_position[1]})')
        continue
    if field[rover_position[0]][rover_position[1]] == 'C':
        concrete_deposits += 1
        print(f'Concrete deposit found at ({rover_position[0]}, {rover_position[1]})')
        continue
    if field[rover_position[0]][rover_position[1]] == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        has_broken = True
        break
    if field[rover_position[0]][rover_position[1]] == '-':
        continue

if not has_broken and water_deposits > 0 and metal_deposits > 0 and concrete_deposits > 0:
    print('Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')

