rows_count = int(input())

matrix = [[x for x in input()] for _ in range(rows_count)]

searched_symbol = input()
location = ()
is_found = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_el = matrix[row][col]

        if current_el == searched_symbol:
            location = (row, col)
            is_found = True
            break

    if is_found:
        break

if is_found:
    print(location)
else:
    print(f'{searched_symbol} does not occur in the matrix')