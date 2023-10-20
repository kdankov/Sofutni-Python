first_name, second_name = input().split(', ')

current_player_position = []

maze = [[x for x in input().split()] for row in range(6)]

first_player_rests = False
second_player_rests = False

while True:
    position = [int(x) for x in input() if x.isalnum()]

    if not first_player_rests:
        if maze[position[0]][position[1]] == 'E':
            print(f'{first_name} found the Exit and wins the game!')
            break
        if maze[position[0]][position[1]] == 'T':
            print(f'{first_name} is out of the game! The winner is {second_name}.')
            break
        if maze[position[0]][position[1]] == 'W':
            print(f'{first_name} hits a wall and needs to rest.')
            first_player_rests = True
    else:
        first_player_rests = False

    position = [int(x) for x in input() if x.isalnum()]

    if not second_player_rests:
        if maze[position[0]][position[1]] == 'E':
            print(f'{second_name} found the Exit and wins the game!')
            break
        if maze[position[0]][position[1]] == 'T':
            print(f'{second_name} is out of the game! The winner is {first_name}.')
            break
        if maze[position[0]][position[1]] == 'W':
            print(f'{second_name} hits a wall and needs to rest.')
            second_player_rests = True
    else:
        second_player_rests = False