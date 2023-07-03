import sys

n = int(input())

max_num = -sys.maxsize
sum = 0

for i in range (n):
    num = int(input())
    
    sum += num
    
    if num > max_num:
        max_num = num

sum -= max_num

if sum == max_num:
    print(f'Yes \nSum = {sum}')
else:
    print(f'No \nDiff = {abs(max_num - sum)}')
    
