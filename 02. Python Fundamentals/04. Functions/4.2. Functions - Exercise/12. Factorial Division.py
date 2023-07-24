from math import factorial

def factiorial_division(a, b):
    return f'{(int(factorial(a) / factorial(b))):.2f}'
    
first_num = int(input())
second_num = int(input())

print(factiorial_division(first_num, second_num))