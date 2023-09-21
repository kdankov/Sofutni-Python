size = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]

primary_diagonal = [matrix[i][i] for i in range(size)]
primary_diagonal_sum = sum(primary_diagonal)

secondary_diagonal = [matrix[i][size - i - 1] for i in range(size)]
secondary_diagonal_sum = sum(secondary_diagonal)


print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {secondary_diagonal_sum}')
