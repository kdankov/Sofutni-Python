control_sum = int(input())

count = 0
password = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == control_sum:
                    count += 1 
                    print(f'{a}{b}{c}{d}', end=' ')
                    
                    if count == 4:
                        password = f'{a}{b}{c}{d}'

if len(password) > 0:
    print(f'\nPassword: {password}')
else:
    print('\nNo!')