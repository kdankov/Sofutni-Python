n = int(input())

even_sum = 0
even_max = 'No'
even_min = 'No'

odd_sum = 0
odd_max = 'No'
odd_min = 'No'


for i in range(1, n + 1):
    num = float(input())
    
    if i % 2 == 0:
        even_sum += num
        
        if even_max == 'No' or num > even_max:
            even_max = num
            
        if even_min == 'No' or num < even_min:
            even_min = num
    else:
        odd_sum += num
        
        if odd_max == 'No' or num > odd_max:
            odd_max = num
            
        if odd_min == 'No' or num < odd_min:
            odd_min = num

print(f'OddSum={odd_sum:.2f},')

if odd_min == 'No':
    print(f'OddMin={odd_min},')
    print(f'OddMax={odd_max},')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
    
print(f'EvenSum={even_sum:.2f},')

if even_min == 'No':
    print(f'EvenMin={even_min},')
    print(f'EvenMax={even_max}')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')