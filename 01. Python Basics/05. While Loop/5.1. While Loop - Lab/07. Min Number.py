import sys

number = input()

min_num = sys.maxsize

while number != 'Stop':
    if int(number) < min_num:
        min_num = int(number)
    
    number = input()

print(min_num)