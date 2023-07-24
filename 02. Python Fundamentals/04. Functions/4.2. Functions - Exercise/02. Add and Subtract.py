def sum_numbers(a, b):
    return a + b
    
def subtract(a, b, c):
    return sum_numbers(a, b) - c
   
   
first_num = int(input()) 
second_num = int(input())
third_num = int(input())

print(subtract(first_num, second_num, third_num))