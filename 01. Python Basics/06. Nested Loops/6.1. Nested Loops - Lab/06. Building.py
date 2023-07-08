floors = int(input())
rooms = int(input())

current_floor = ''

for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i == floors:
            current_floor += f'L{i}{j}' + ' '
        elif i % 2 == 0:
            current_floor += f'O{i}{j}' + ' '
        else:
            current_floor += f'A{i}{j}' + ' '

    print(current_floor)
    current_floor = ''
