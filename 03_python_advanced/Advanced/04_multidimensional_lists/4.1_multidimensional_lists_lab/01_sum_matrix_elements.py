rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

sum_of_all_numbers = 0

for el in matrix:
    sum_of_all_numbers += sum(el)

print(sum_of_all_numbers)
print(matrix)
