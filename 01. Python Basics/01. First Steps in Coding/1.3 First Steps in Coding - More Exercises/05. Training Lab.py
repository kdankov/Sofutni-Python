from math import floor

height = float(input())
width = float(input())

height *= 100
width *= 100

free_width = width - 100
count_desks_row = floor(free_width / 70)
count_desks_column = floor(height / 120)
totalSeats = (count_desks_row * count_desks_column) - 3

print(totalSeats)

