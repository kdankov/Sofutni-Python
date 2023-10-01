def is_valid(r, c, size):
    return 0 <= r < size and 0 <= c < size


rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()

while command != 'END':
    args = command.split()
    operation = args[0]
    row = int(args[1])
    col = int(args[2])
    value = int(args[3])

    if is_valid(row, col, len(matrix)):
        if operation == 'Add':
            matrix[row][col] += value
        elif operation == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    command = input()
[print(*row) for row in matrix]
