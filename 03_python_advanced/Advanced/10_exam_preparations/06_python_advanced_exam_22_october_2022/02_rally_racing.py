size = int(input())
car_number = input()
race_route = []
kilometers_passed = 0
car_coordinates = [0, 0]

for _ in range(size):
    race_route.append(input().split())


def find_end_of_dune(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "T":
                return row, col


possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()

    if command == 'End':
        race_route[car_coordinates[0]][car_coordinates[1]] = 'C'
        print(f"Racing car {car_number} DNF.")
        break

    next_move = possible_moves[command]
    car_coordinates[0] += next_move[0]
    car_coordinates[1] += next_move[1]

    if race_route[car_coordinates[0]][car_coordinates[1]] == 'F':
        kilometers_passed += 10
        race_route[car_coordinates[0]][car_coordinates[1]] = 'C'
        print(f'Racing car {car_number} finished the stage!')
        break

    elif race_route[car_coordinates[0]][car_coordinates[1]] == 'T':
        kilometers_passed += 30
        race_route[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_end_of_dune(race_route)
        race_route[car_coordinates[0]][car_coordinates[1]] = "."

    else:
        kilometers_passed += 10

print(f"Distance covered {kilometers_passed} km.")
for row in range(len(race_route)):
    print("".join(race_route[row]))
