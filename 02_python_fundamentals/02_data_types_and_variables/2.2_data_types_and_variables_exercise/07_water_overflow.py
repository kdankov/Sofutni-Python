n = int(input())

capacity = 0

for i in range(n):
    current_liters = int(input())
    
    if capacity + current_liters > 255:
        print('Insufficient capacity!')
        continue
    
    capacity += current_liters

print(capacity)
