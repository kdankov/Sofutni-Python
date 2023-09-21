rows, cols = [int(x) for x in input().split(", ")]
matrix = []

sum_of_all_numbers = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sum_of_all_numbers += sum(lines)
    matrix.append(lines)

print(sum_of_all_numbers)
print(matrix)
