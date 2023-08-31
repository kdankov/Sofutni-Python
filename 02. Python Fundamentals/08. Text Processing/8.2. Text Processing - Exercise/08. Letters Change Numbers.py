line = input().split()

multiply_or_divide = 0
result_number = 0
total_sum = 0

for word in line:
    first_symbol = word[0]
    last_symbol = word[-1]
    
    position_first = ord(first_symbol.upper()) - 64
    position_last = ord(last_symbol.upper()) - 64
    
    word = word[1:len(word) - 1]
    
    number = int(word)
    
    if first_symbol.isupper():
        multiply_or_divide = number / position_first
    else:
        multiply_or_divide = number * position_first
        
    if last_symbol.isupper():
        result_number = multiply_or_divide - position_last
    else:
        result_number = multiply_or_divide + position_last
        
    total_sum += result_number

print(f'{total_sum:.2f}')