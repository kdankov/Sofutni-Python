def are_valid_indices(index1, index2, check_matrix):
    return 0 <= index1 < len(check_matrix) and 0 <= index2 < len(check_matrix[index1])


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

bombs_coordinates = input().split()

for coordinates in bombs_coordinates:
    bomb_row, bomb_col = [int(x) for x in coordinates.split(",")]
    bomb_value = matrix[bomb_row][bomb_col]

    if bomb_value <= 0:
        continue
    else:
        matrix[bomb_row][bomb_col] = 0

    for row in range(bomb_row - 1, bomb_row + 2):
        for col in range(bomb_col - 1, bomb_col + 2):
            if are_valid_indices(row, col, matrix) and matrix[row][col] > 0:
                matrix[row][col] -= bomb_value

alive_cells = []

for r in matrix:
    alive_cells.extend([x for x in r if x > 0])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*m_row) for m_row in matrix]