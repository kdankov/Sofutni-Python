first_row = [int(x) for x in input().split(' ')]
second_row = [int(x) for x in input().split(' ')]
third_row = [int(x) for x in input().split(' ')]

if (first_row[0] == second_row[0] == third_row[0] == 1) or \
    (first_row[1] == second_row[1] == third_row[1] == 1) or \
    (first_row[2] == second_row[2] == third_row[2] == 1) or \
    (first_row[0] == first_row[1] == first_row[2] == 1) or \
    (second_row[0] == second_row[1] == second_row[2] == 1) or \
    (third_row[0] == third_row[1] == third_row[2] == 1) or \
    (first_row[0] == second_row[1] == third_row[2] == 1) or \
    (first_row[2] == second_row[1] == third_row[0] == 1):
        print('First player won')
elif (first_row[0] == second_row[0] == third_row[0] == 2) or \
    (first_row[1] == second_row[1] == third_row[1] == 2) or \
    (first_row[2] == second_row[2] == third_row[2] == 2) or \
    (first_row[0] == first_row[1] == first_row[2] == 2) or \
    (second_row[0] == second_row[1] == second_row[2] == 2) or \
    (third_row[0] == third_row[1] == third_row[2] == 2) or \
    (first_row[0] == second_row[1] == third_row[2] == 2) or \
    (first_row[2] == second_row[1] == third_row[0] == 1):
        print('Second player won')
else:
        print('Draw!')

