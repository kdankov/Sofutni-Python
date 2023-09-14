first_num_max = int(input())
second_num_max = int(input())
third_num_max = int(input())

for i in range(2, first_num_max + 1, 2):
    for j in range(2, second_num_max + 1):
        if (j == 2 or j == 3 or j == 5 or j == 7):
            for k in range(2, third_num_max + 1, 2):
                print(f'{i} {j} {k}')