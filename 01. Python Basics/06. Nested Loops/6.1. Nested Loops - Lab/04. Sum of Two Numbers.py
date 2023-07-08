start = int(input())
end = int(input())
magic_num = int(input())

combination_num = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combination_num += 1
        if i + j == magic_num:
            print(f'Combination N:{combination_num} ({i} + {j} = {magic_num})')
            is_found = True
    
    if is_found:
        break

if not is_found:
    print(f'{combination_num} combinations - neither equals {magic_num}')