n = int(input())

is_speical = False

for number in range(1000, 9999):
    num_to_str = str(number)
    
    for digit in num_to_str:
        if digit == '0':
            is_speical = False
            break
        
        if n % int(digit) == 0:
            is_speical = True
        else:
            is_speical = False
            break
    
    if is_speical:
        print(number, end=' ')