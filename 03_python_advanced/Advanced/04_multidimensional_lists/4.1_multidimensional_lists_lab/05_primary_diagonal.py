size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

primary_diagonal_sum = sum(matrix[size - i - 1][size - i - 1] for i in range(size))

print(primary_diagonal_sum)