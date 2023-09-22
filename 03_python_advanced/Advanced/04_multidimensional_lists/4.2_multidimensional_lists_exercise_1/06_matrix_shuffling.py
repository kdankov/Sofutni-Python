def is_valid(num, border):
    if 0 <= num < border:
        return True
    return False


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

command = input()

while command != 'END':
    tokens = command.split()
    operation = tokens[0]

    if len(tokens) == 5 and operation == 'swap':
        row1 = int(tokens[1])
        col1 = int(tokens[2])

        row2 = int(tokens[3])
        col2 = int(tokens[4])

        if is_valid(row1, rows) and is_valid(col1, cols) and is_valid(row2, rows) and is_valid(col2, cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
            command = input()
            continue
    else:
        print('Invalid input!')

    command = input()
