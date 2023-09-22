rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    current_row = []
    for col in range(cols):
        first_and_last_letter = chr(row + 97)
        middle_letter = chr(col + row + 97)

        current_row += [f'{first_and_last_letter}{middle_letter}{first_and_last_letter}']

    matrix.append(current_row)

[print(*row) for row in matrix]