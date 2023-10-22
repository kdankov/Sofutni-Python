size = int(input())

fishing_area = []
ship_position = []

for row in range(size):
    fishing_area.append(list(input()))
    for col in range(size):
        if fishing_area[row][col] == 'S':
            ship_position = [row, col]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()
fish_caught = 0
has_fallen = False

while command != 'collect the nets':
    current_move = possible_moves[command]
    row = ship_position[0] + current_move[0]
    col = ship_position[1] + current_move[1]

    if row < 0:
        row = size - 1
    elif row > size - 1:
        row = 0
    elif col < 0:
        col = size - 1
    elif col > size - 1:
        col = 0

    if fishing_area[row][col].isdigit():
        fish_caught += int(fishing_area[row][col])

    elif fishing_area[row][col] == 'W':
        ship_position = [row, col]
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the '
              f'ship: [{ship_position[0]},{ship_position[1]}]')
        has_fallen = True
        break

    elif fishing_area[row][col] == '-':
        pass

    fishing_area[ship_position[0]][ship_position[1]] = '-'
    ship_position = [row, col]
    fishing_area[row][col] = 'S'

    command = input()

if not has_fallen:
    if fish_caught >= 20:
        print('Success! You managed to reach the quota!')
    else:
        print(f'You didn\'t catch enough fish and didn\'t reach the quota! You need {20 - fish_caught} tons of fish more.')

    if fish_caught > 0:
        print(f'Amount of fish caught: {fish_caught} tons.')
    [print(*row, sep='') for row in fishing_area]