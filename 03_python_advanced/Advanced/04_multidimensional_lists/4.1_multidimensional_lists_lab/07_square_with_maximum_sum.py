rows, cols = input().split(', ')
rows = int(rows)
cols = int(cols)

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
max_sum_sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        right_element = matrix[row][col + 1]
        below_element = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]

        current_sum = current_element + right_element + below_element + diagonal_element

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_sub_matrix = [
                [current_element, right_element],
                [below_element, diagonal_element]
            ]

print(*max_sum_sub_matrix[0])
print(*max_sum_sub_matrix[1])
print(max_sum)