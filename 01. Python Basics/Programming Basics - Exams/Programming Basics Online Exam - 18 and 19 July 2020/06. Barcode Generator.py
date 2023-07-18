start_num = int(input())
end_num = int(input())

first_start = int(start_num / 1000);
second_start = int((start_num / 100) % 10);
third_start = int((start_num / 10) % 10);
fourth_start = int(start_num % 10);
    
first_end = int(end_num / 1000);
second_end = int((end_num / 100) % 10);
third_end = int((end_num / 10) % 10);
fourth_end = int(end_num % 10);

for i in range(first_start, first_end + 1):
    for j in range(second_start, second_end + 1):
        for k in range(third_start, third_end + 1):
            for l in range(fourth_start, fourth_end + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f'{i}{j}{k}{l}', end=' ')