def odd_even_sum(num):
    even_digits_sum = 0
    odd_digits_sum = 0
    
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_digits_sum += int(digit)
        elif int(digit) % 2 != 0:
            odd_digits_sum += int(digit)
    
    return f'Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}'

number = int(input())

print(odd_even_sum(number))
