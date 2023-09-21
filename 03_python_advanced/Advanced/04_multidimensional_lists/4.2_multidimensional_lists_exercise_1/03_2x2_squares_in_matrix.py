rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for row in range(rows)]

count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        right_element = matrix[row][col + 1]
        below_element = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]

        if current_element == right_element == below_element == diagonal_element:
            count += 1

print(count)