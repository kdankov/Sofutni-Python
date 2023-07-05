import sys

number = input()

max_num = -sys.maxsize

while number != 'Stop':
    if int(number) > max_num:
        max_num = int(number)
    
    number = input()

print(max_num)